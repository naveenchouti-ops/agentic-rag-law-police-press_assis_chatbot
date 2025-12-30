from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from pathlib import Path

# 📄 Load press texts
press_files = [
    Path("text/press_pci.txt"),
    Path("text/press_pib.txt")
]

documents = []
for file in press_files:
    documents.append(file.read_text(encoding="utf-8"))

full_text = "\n".join(documents)

# ✂️ Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
chunks = splitter.split_text(full_text)

print(f"Total press chunks: {len(chunks)}")

# 🔢 Embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)

# 📦 Vector DB (PRESS)
vectordb = Chroma.from_texts(
    texts=chunks,
    embedding=embedding,
    persist_directory="vectordb/press_db"
)

vectordb.persist()
print("✅ Press vector DB created successfully")
