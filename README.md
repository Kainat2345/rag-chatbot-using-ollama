# 🏏 Cricket RAG Chatbot (Ollama + ChromaDB + Streamlit)

A powerful **Retrieval-Augmented Generation (RAG)** chatbot that answers cricket-related questions using a local knowledge base, vector search (ChromaDB), and LLMs via Ollama — all wrapped in a ChatGPT-style Streamlit UI.

---

## 🚀 Features

* 🧠 RAG-based question answering system
* 📚 PDF / text knowledge ingestion
* 🔍 Vector search using **ChromaDB**
* 🤖 Local LLM support via **Ollama (Llama3 / Mistral)**
* 🧾 Embeddings using `nomic-embed-text`
* 💬 ChatGPT-like UI with Streamlit
* 🧠 Conversation memory (session-based chat history)
* ⚡ Fully local (no OpenAI API required)

---

## 🛠️ Tech Stack

* Python 3.11
* Streamlit
* LangChain
* ChromaDB
* Ollama
* Nomic Embeddings
* PyPDF

---

## 📁 Project Structure

```
rag_based chatbot/
│
├── app.py              # Streamlit Chat UI
├── ingest.py           # Data ingestion + embeddings
├── chroma_db/          # Vector database (auto-generated)
├── data/               # Source documents (PDF/text)
├── rag_env/            # Virtual environment (ignored in git)
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

---

### 2. Create virtual environment

```bash
python3.11 -m venv rag_env
source rag_env/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install streamlit langchain langchain-community chromadb sentence-transformers pypdf ollama
```

---

### 4. Install & run Ollama

Install Ollama:
👉 https://ollama.com

Then run:

```bash
ollama serve
ollama pull llama3
ollama pull nomic-embed-text
```

---

## 📥 Data Ingestion

Before running the app, build vector database:

```bash
python ingest.py
```

This will:

* Load documents
* Split into chunks
* Generate embeddings
* Store in ChromaDB

---

## ▶️ Run Application

```bash
python -m streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 💬 How it works

1. User asks a question
2. Query is embedded using Ollama embeddings
3. ChromaDB retrieves relevant chunks
4. LLM (Llama3) generates final answer
5. Streamlit displays ChatGPT-style response

---

## 🧠 Example Questions

* When was the first Cricket World Cup played?
* Who is the highest run scorer in ODI cricket?
* What is Test cricket?
* Biography of Babar Azam

---

## ⚠️ Requirements

* Python 3.11 recommended
* Ollama installed and running
* At least 4–8GB RAM for LLM

---

## 🧑‍💻 Author

Built by **KAINAT**
AI + RAG + LLM Learning Project

---

## ⭐ Future Improvements

* PDF upload UI
* Streaming responses
* Persistent chat history
* Multi-document QA
* FastAPI backend version
* Docker deployment

---

## 📜 License

This project is for educational purposes.
