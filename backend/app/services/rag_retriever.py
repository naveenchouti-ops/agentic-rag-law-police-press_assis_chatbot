from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def retrieve_context(query: str, db_path: str, k: int = 4) -> str:
    # Force CPU to avoid dtype mismatch between float32 inputs and float16 model weights
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    vectordb = Chroma(
        persist_directory=db_path,
        embedding_function=embedding
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": k})

    # docs = retriever.get_relevant_documents(query)
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])
    return context
