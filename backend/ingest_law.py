from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from pathlib import Path


# Load LAW text files
ipc = Path("text/law_ipc.txt").read_text(encoding="utf-8")
crpc = Path("text/law_crpc.txt").read_text(encoding="utf-8")

full_text = ipc + "\n" + crpc

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_text(full_text)
print("Total chunks:", len(chunks))

# Create embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in vector DB
db = Chroma.from_texts(
    chunks,
    embedding,
    persist_directory="vectordb/law_db"
)

db.persist()
print("✅ Law vector DB created")
