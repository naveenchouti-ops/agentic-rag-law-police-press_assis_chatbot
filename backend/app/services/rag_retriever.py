from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


def retrieve_context(query: str, db_path: str, k: int = 4) -> str:
    """
    Retrieve relevant context from a vector database using semantic search.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate input parameters (query and db_path must be non-empty)
    2. Initialize the embedding model (sentence-transformers for semantic understanding)
    3. Load the vector database from the specified path
    4. Create a retriever that will find the k most relevant documents
    5. Search the database using the query to find semantically similar documents
    6. Combine all retrieved document contents into a single context string
    7. Return the combined context for use in prompt engineering
    
    Args:
        query (str): The search query to find relevant context
        db_path (str): File path to the vector database directory
        k (int, optional): Number of top documents to retrieve. Defaults to 4.
        
    Returns:
        str: Combined text content from retrieved documents
        
    Edge cases handled:
    - Empty or None query: Returns empty string
    - Invalid or missing db_path: Caught by try-except, returns empty string
    - k less than 1: Clamped to minimum of 1
    - No matching documents: Returns empty string
    - Database errors: Caught and handled gracefully
    """
    try:
        # Edge case: Validate query
        if not query or not isinstance(query, str) or not query.strip():
            return ""
        
        # Edge case: Validate db_path
        if not db_path or not isinstance(db_path, str):
            return ""
        
        # Edge case: Ensure k is at least 1
        k = max(1, int(k)) if k else 4
        
        # Step 1: Initialize embedding model for semantic understanding
        embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Step 2: Load vector database from specified path
        vectordb = Chroma(
            persist_directory=db_path,
            embedding_function=embedding
        )

        # Step 3: Create retriever with k documents
        retriever = vectordb.as_retriever(search_kwargs={"k": k})

        # Step 4: Retrieve relevant documents using semantic search
        docs = retriever.invoke(query.strip())
        
        # Edge case: No documents found
        if not docs:
            return ""

        # Step 5: Combine all document contents into single context string
        context = "\n\n".join([doc.page_content for doc in docs if doc.page_content])
        
        return context
        
    except Exception as e:
        # Edge case: Handle database errors gracefully
        print(f"⚠️ RAG Retrieval Error: {e}")
        return ""
