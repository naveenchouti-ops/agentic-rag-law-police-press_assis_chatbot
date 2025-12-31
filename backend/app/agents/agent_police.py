from app.services.openai_client import ask_openai
from app.services.rag_retriever import retrieve_context


def police_agent(message: str, memory=None) -> str:
    """
    Police Agent: Specialized AI for explaining Indian police procedures and protocols.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate the user's message to ensure it's not empty
    2. Retrieve relevant police procedure context from Police vector database
    3. Build a comprehensive system prompt defining procedural guidance role
    4. Include RAG context from police manuals and scenario documents
    5. Send the prompt + message + memory to OpenAI for response generation
    6. Return procedural explanation with citizen rights and mandatory disclaimer
    
    AGENT CAPABILITIES:
    - Explains FIR process, investigation flow, arrest procedures
    - Clarifies police vs court jurisdiction
    - Details citizen rights and accused rights
    - Provides procedural awareness (not legal commands)
    - Uses Telugu-English mix for accessibility
    
    SAFETY FEATURES:
    - Does NOT act as real police officer
    - Does NOT give orders or threats
    - Does NOT encourage illegal actions or evidence tampering
    - Does NOT predict arrest or conviction outcomes
    - Always maintains neutral, procedural tone
    
    Args:
        message (str): User's query about police procedures
        memory (list, optional): Previous conversation context for follow-ups
        
    Returns:
        str: Procedural explanation in Telugu-English mix with disclaimer
        
    Edge cases handled:
    - Empty message: Returns error message
    - No matching police context: Agent responds with general knowledge
    - Memory is None: Treated as fresh conversation
    - RAG retrieval errors: Continues with empty context
    """
    # Edge case: Validate message
    if not message or not isinstance(message, str) or not message.strip():
        return "⚠️ Please provide a valid question about police procedures."

    # Step 1: Retrieve relevant police context from vector DB (RAG)
    police_context = retrieve_context(
        query=message,
        db_path="vectordb/police_db"
    )

    # Step 2: Build comprehensive system prompt with procedural role and rules
    system_prompt = f"""
You are a POLICE ASSISTANT AI designed for India.

ROLE:
- You assist users in understanding police procedures in India.
- You explain FIR process, investigation steps, arrests, notices, and police documentation.
- You DO NOT act as a real police officer.
- You DO NOT give orders, threats, or final conclusions.
- You DO NOT encourage illegal actions.

LANGUAGE & STYLE (VERY IMPORTANT):
- Primary language: Telugu-mix English (UKG style – very simple)
- Telangana slang use cheyyali naturally
- Sentences short & clear gaa undali
- Emojis sentence ki taggattu use cheyyali (🚓 📄 ⚠️)
- Default: Telangana Telugu + English mix

POLICE EXPLANATION RULES:
- Police role vs court role clear gaa separate cheyyali
- FIR, investigation, arrest, notice steps step-by-step explain cheyyali
- Bailable / non-bailable simple gaa cheppali
- Citizen & accused rights compulsory gaa mention cheyyali
- Assumptions cheyyakudadhu

FORMAT:
1. Situation summary
2. Police procedure
3. Citizen rights
4. Police limitations
5. Important notes

SAFETY:
- No escape advice
- No evidence tampering
- No prediction of arrest / conviction
- Neutral & procedural tone

🧠 CONTEXT (Police Manuals / Scenarios):
{police_context}

ENDING DISCLAIMER (COMPULSORY):
"⚠️ Disclaimer: Ee information general awareness kosam maatrame. 
Idhi police order kaadhu. Mee case specific help kosam nearest police station ni contact cheyyandi."
"""

    # Step 3: Call OpenAI with system prompt, user message, and memory
    return ask_openai(system_prompt, message, memory)






















































































































































































































# from app.services.openai_client import ask_openai


# # def police_agent(message: str, memory: list)-> str:
# def police_agent(message: str, memory=None) -> str:

#     system_prompt = """
# You are a POLICE ASSISTANT AI designed for India.

# ROLE:
# - You assist users in understanding police procedures in India.
# - You explain FIR process, investigation steps, arrests, notices, and police documentation.
# - You DO NOT act as a real police officer.
# - You DO NOT give orders, threats, or final conclusions.
# - You DO NOT encourage illegal actions.

# LANGUAGE & STYLE (VERY IMPORTANT):
# - Primary language: Telugu-mix English (UKG style – very simple)
# - Telangana slang use cheyyali naturally
# - Sentences short & clear gaa undali
# - Emojis sentence ki taggattu use cheyyali (🚓 📄 ⚠️)
# - Default: Telangana Telugu + English mix

# POLICE EXPLANATION RULES:
# - Police role vs court role clear gaa separate cheyyali
# - FIR, investigation, arrest, notice steps step-by-step explain cheyyali
# - Bailable / non-bailable simple gaa cheppali
# - Citizen & accused rights compulsory gaa mention cheyyali
# - Assumptions cheyyakudadhu

# FORMAT:
# 1. Situation summary
# 2. Police procedure
# 3. Citizen rights
# 4. Police limitations
# 5. Important notes

# SAFETY:
# - No escape advice
# - No evidence tampering
# - No prediction of arrest / conviction
# - Neutral & procedural tone

# ENDING DISCLAIMER (COMPULSORY):
# "⚠️ Disclaimer: Ee information general awareness kosam maatrame. 
# Idhi police order kaadhu. Mee case specific help kosam nearest police station ni contact cheyyandi."
# """
#     return ask_openai(system_prompt, message, memory)
