import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

st.title("🏏 Cricket RAG Chatbot (Ollama Edition)")

# Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Load DB
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# LLM
llm = Ollama(model="llama3")

question = st.text_input("Ask a question")

if question:

    docs = retriever.invoke(question)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a cricket assistant.

Use only this context:
{context}

Question: {question}

Answer clearly:
"""

    response = llm.invoke(prompt)

    st.write(response)