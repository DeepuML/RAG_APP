<h1 align="center">🧠 RAG App for Meta SuperIntelligent Lab</h1>

<p align="center">
  <b>A Retrieval-Augmented Generation (RAG) system</b> that allows users to query a domain-specific knowledge base related to Meta's SuperIntelligent Lab and receive intelligent, contextual answers using LLMs.
</p>

---

## 🚀 Project Overview

This application is a **RAG-based Question Answering System** built with:

- 🔍 **FAISS** for semantic search and retrieval
- 🧠 **LLM (via OpenAI/EURI)** for contextual text generation
- 🧱 **Embeddings** via `text-embedding-3-small`
- 🎨 **Streamlit** for an interactive and responsive user interface

Users can ask questions related to Meta SuperIntelligent Lab's projects, goals, documents, and research, and receive intelligent answers based on pre-embedded data chunks.

---

## 📂 Folder Structure

Meta-RAG-App/

├── app.py # Main Streamlit app

├── .env # Contains EURI_API_KEY

├── requirements.txt # Required dependencies

└── utils/

├── embedding.py # Embedding functions

├── chunking.py # Text chunking utilities

├── retrieval.py # FAISS-based retrieval

├── prompt.py # Prompt generation

└── completion.py # LLM completion handler


## 🧰 Features

- ✅ Natural Language QA over lab-specific knowledge
- ✅ Modular codebase for chunking, embedding, retrieval, and generation
- ✅ FAISS-based fast semantic retrieval
- ✅ Custom prompts for improved LLM response quality
- ✅ Live UI using Streamlit with response transparency
- ✅ Error handling and debug info built-in

---

## ⚙️ Installation

1. **Clone the repository**

git clone https://github.com/yourusername/meta-rag-app.git
cd meta-rag-app

▶️ Running the App : streamlit run app.py

📌 Screenshots

<img width="1895" height="636" alt="image" src="https://github.com/user-attachments/assets/561e57f1-2d45-4f82-aaf7-670b9b6496fd" />

<h2 align="center">🧠 Tech Stack</h2>

- **Streamlit** – Web Interface  
- **FAISS** – Vector Store for Document Retrieval  
- **EURI API** – Embeddings & Completion Models  
- **Python** – Core Application Logic  

---

<h2 align="center">🤝 Contribution</h2>

Contributions are welcome! Please open issues or submit pull requests.

---

<h2 align="center">📄 License</h2>

This project is licensed under the MIT License.
