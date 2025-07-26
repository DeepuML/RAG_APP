import streamlit as st
from utils.embedding import get_embedding
from utils.chunking import chunk_text
from utils.retrieval import load_faiss_index, retrieve_chunks
from utils.prompt import build_prompt
from utils.completion import generate_completion

# --------------------- UI Layout ---------------------
st.set_page_config(page_title="RAG Chatbot | Meta SuperIntelligent Lab", layout="wide")
st.title("🧠 RAG App for Meta SuperIntelligent Lab")
st.markdown("Ask me anything related to the lab's research, tools, or vision.")

st.sidebar.header("🔧 RAG System Info")
st.sidebar.markdown("""
- **Embedding Model:** `text-embedding-3-small`
- **Completion Model:** `gpt-4.1-nano`
- **Vector DB:** FAISS
""")

# --------------------- Query Input ---------------------
query = st.text_input("💬 Enter your question:", placeholder="e.g. What is the goal of the Meta SuperIntelligent Lab?")

if query:
    with st.spinner("🔍 Searching knowledge base..."):
        try:
            index, chunk_mapping = load_faiss_index()
            top_chunks = retrieve_chunks(query, index, chunk_mapping)
            prompt = build_prompt(top_chunks, query)
            response = generate_completion(prompt)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    # --------------------- Response Display ---------------------
    st.success("✅ Answer Generated:")
    st.markdown(f"**{response}**")

    # --------------------- Debug Info ---------------------
    with st.expander("📄 Retrieved Chunks"):
        for i, chunk in enumerate(top_chunks, 1):
            st.markdown(f"**Chunk {i}:** {chunk}")

    with st.expander("🧾 Prompt Sent to LLM"):
        st.code(prompt, language='markdown')
