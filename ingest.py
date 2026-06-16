from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Load PDF
loader = PyPDFLoader("data/cricket.pdf")
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

# OLLAMA EMBEDDINGS (NO TORCH)
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Store in Chroma
db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="chroma_db"
)

db.persist()

print("Vector DB created successfully")