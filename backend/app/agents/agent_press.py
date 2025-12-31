from app.services.openai_client import ask_openai
from app.services.rag_retriever import retrieve_context


def press_agent(message: str, memory=None) -> str:
    """
    Press Agent: Specialized AI for news reporting with journalistic ethics.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate the user's message to ensure it's not empty
    2. Retrieve relevant press context from Press vector database (PCI guidelines, PIB)
    3. Build a comprehensive system prompt defining journalistic role and ethics
    4. Include RAG context from Press Council of India and official releases
    5. Send the prompt + message + memory to OpenAI for response generation
    6. Return news-style report with fact-checking awareness and disclaimer
    
    AGENT CAPABILITIES:
    - Writes news articles, headlines, reports in journalistic style
    - Follows Indian Press Council ethics strictly
    - Maintains neutral, factual tone without sensationalism
    - Distinguishes facts from assumptions clearly
    - Uses Telugu-English mix for accessibility
    
    SAFETY FEATURES:
    - Does NOT conduct media trials or pass judgments
    - Does NOT confirm guilt or innocence
    - Does NOT name minors or violate privacy
    - Does NOT use sensational or provocative language
    - Respects victim dignity and privacy
    - No verdict predictions
    
    Args:
        message (str): User's query about news reporting or event coverage
        memory (list, optional): Previous conversation context for follow-ups
        
    Returns:
        str: News-style report in Telugu-English mix with disclaimer
        
    Edge cases handled:
    - Empty message: Returns error message
    - No matching press context: Agent responds with general knowledge
    - Memory is None: Treated as fresh conversation
    - RAG retrieval errors: Continues with empty context
    """
    # Edge case: Validate message
    if not message or not isinstance(message, str) or not message.strip():
        return "⚠️ Please provide a valid query for news reporting."

    # Step 1: Retrieve relevant press context from vector DB (RAG)
    press_context = retrieve_context(
        query=message,
        db_path="vectordb/press_db"
    )

    # Step 2: Build comprehensive system prompt with journalistic role and ethics
    system_prompt = f"""
You are a PRESS / MEDIA ASSISTANT AI designed for Indian print and electronic media.

ROLE:
- You act like a professional journalist / news reporter.
- You write news articles, headlines, reports, and summaries.
- You strictly follow Indian journalistic ethics.
- You DO NOT give legal judgments.
- You DO NOT act as police or court.
- You DO NOT confirm guilt or innocence.

LANGUAGE & STYLE (VERY IMPORTANT):
- Primary language: Simple Telugu-mix English (UKG style)
- Neutral Telugu (no regional slang)
- Short and clear sentences
- Emojis limited gaa (📰 📺 ⚠️)
- Default: Neutral Telugu + English mix

JOURNALISM RULES (STRICT):
- Facts vs assumptions separate gaa cheppali
- Use phrases like "according to sources", "as per police"
- Neutral tone maintain cheyyali
- No sensational language ❌
- Respect victim dignity & privacy

FORMAT:
1. Headline
2. Location + time
3. What happened (facts only)
4. Official statements
5. Confirmed vs unconfirmed
6. Public advisory (if needed)

SAFETY:
- No media trials
- No naming minors
- No verdict prediction
- No hate or provocation

🧠 CONTEXT (Press Council of India / PIB Releases):
{press_context}

ENDING DISCLAIMER (COMPULSORY):
"⚠️ Disclaimer: Ee report available information adharam gaa tayaaru chesindi.
Idhi investigation result kaadhu lekapothe court judgement kaadhu.
Samayam tho information maaravachu."
"""

    # Step 3: Call OpenAI with system prompt, user message, and memory
    return ask_openai(system_prompt, message, memory)
