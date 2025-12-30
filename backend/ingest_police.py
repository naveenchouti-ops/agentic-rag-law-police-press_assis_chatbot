from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from pathlib import Path

# 📄 Load police text
police_file = Path("text/police_scenarios.txt")

text = police_file.read_text(encoding="utf-8")

# ✂️ Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
chunks = splitter.split_text(text)

print(f"Total police chunks: {len(chunks)}")

# 🔢 Embeddings
# Force CPU to avoid dtype mismatch between float32 inputs and float16 model weights
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
)

# 📦 Vector DB (POLICE)
vectordb = Chroma.from_texts(
    texts=chunks,
    embedding=embedding,
    persist_directory="vectordb/police_db"
)

vectordb.persist()
print("✅ Police vector DB created successfully")
