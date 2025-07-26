import faiss
import numpy as np
import pickle
import os

from utils.embedding import get_embedding
from utils.chunking import chunk_text

def load_faiss_index():
    index_path = "faiss_store/index.faiss"
    mapping_path = "faiss_store/chunk_mapping.pkl"
    story_path = "data/data.txt"

    # Ensure file paths exist
    if not os.path.exists(story_path):
        raise FileNotFoundError(f"❌ Required file missing: {story_path}")

    valid_index = os.path.exists(index_path) and os.path.getsize(index_path) > 0
    valid_mapping = os.path.exists(mapping_path) and os.path.getsize(mapping_path) > 0

    if valid_index and valid_mapping:
        try:
            index = faiss.read_index(index_path)
            with open(mapping_path, "rb") as f:
                chunk_mapping = pickle.load(f)
            return index, chunk_mapping
        except Exception as e:
            print("⚠️ Corrupted index or mapping detected. Rebuilding...", e)

    # Rebuild if not valid
    print("🔄 Generating new FAISS index from founder_story.txt...")

    with open(story_path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        raise ValueError(f"⚠️ The file {story_path} is empty. Please add valid content.")

    chunks = chunk_text(text)
    if not chunks:
        raise ValueError("⚠️ No chunks created from the input text. Check chunking logic.")

    chunk_mapping = []
    all_embeddings = []

    for chunk in chunks:
        emb = get_embedding(chunk)
        if emb is not None:
            all_embeddings.append(emb)
            chunk_mapping.append(chunk)

    if not all_embeddings:
        raise ValueError("⚠️ Embeddings could not be generated. Please check get_embedding().")

    all_embeddings = np.array(all_embeddings).astype("float32")
    dimension = all_embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(all_embeddings)

    os.makedirs("faiss_store", exist_ok=True)
    faiss.write_index(index, index_path)
    with open(mapping_path, "wb") as f:
        pickle.dump(chunk_mapping, f)

    print("✅ FAISS index built and saved.")
    return index, chunk_mapping


def retrieve_chunks(query, index, chunk_mapping, k=3):
    try:
        query_vec = get_embedding(query)
        if query_vec is None:
            raise ValueError("Embedding for the query could not be generated.")
        distances, indices = index.search(np.array([query_vec]).astype("float32"), k)
        return [chunk_mapping[i] for i in indices[0]]
    except Exception as e:
        print("❌ Retrieval failed:", e)
        return []
