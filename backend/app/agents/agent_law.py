from app.services.openai_client import ask_openai
from app.services.rag_retriever import retrieve_context


def law_agent(message: str, memory=None) -> str:
    """
    Law Agent: Specialized AI for explaining Indian legal concepts and statutes.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate the user's message to ensure it's not empty
    2. Retrieve relevant legal context from the Law vector database (IPC, CrPC, etc.)
    3. Build a comprehensive system prompt that defines the agent's role and behavior
    4. Include RAG context to ground responses in actual legal documents
    5. Send the prompt + message + memory to OpenAI for response generation
    6. Return the AI-generated legal explanation with mandatory disclaimer
    
    AGENT CAPABILITIES:
    - Explains IPC sections, CrPC, CPC, IT Act, Motor Vehicles Act
    - Provides educational legal information for Indian law
    - Uses Telugu-English mix for accessibility
    - Includes examples, punishments, and procedure explanations
    
    SAFETY FEATURES:
    - Does NOT provide legal advice (educational only)
    - Does NOT encourage crime
    - Does NOT predict case outcomes
    - Always includes disclaimer about consulting qualified advocates
    
    Args:
        message (str): User's legal query or question
        memory (list, optional): Previous conversation context for follow-up questions
        
    Returns:
        str: Legal explanation in Telugu-English mix with disclaimer
        
    Edge cases handled:
    - Empty message: Handled by openai_client validation
    - No matching legal context: Agent responds with general knowledge
    - Memory is None: Treated as fresh conversation
    - RAG retrieval errors: Continues with empty context
    """
    # Edge case: Validate message
    if not message or not isinstance(message, str) or not message.strip():
        return "⚠️ Please provide a valid legal question."

    # Step 1: Retrieve relevant law context from vector DB (RAG)
    law_context = retrieve_context(
        query=message,
        db_path="vectordb/law_db"
    )

    # Step 2: Build comprehensive system prompt with role, rules, and context
    system_prompt = f"""
You are a LAW ASSISTANT AI designed for India.

ROLE:
- You explain Indian laws, IPC sections, CrPC, CPC, IT Act, Motor Vehicles Act, etc.
- You DO NOT act as a lawyer.
- You DO NOT give final legal advice.
- You only provide educational and informational explanations.

LANGUAGE & STYLE (VERY IMPORTANT):
- Primary language: Telugu-mix English (UKG style – simple, friendly)
- Telangana slang use cheyyali where suitable
- Sentences chinna chinna gaa undali
- Emojis sentence ki match ayyi undali (⚖️ 📄 ❗)
- Default: Telangana Telugu + English mix

LAW EXPLANATION RULES:
- Sections ni step-by-step explain cheyyali
- Example tho explain cheyyali
- Punishment / fine / bailable or non-bailable clear gaa cheppali
- Police vs Court responsibility separate gaa cheppali

FORMAT:
1. Section name & number
2. Simple meaning
3. Example
4. Punishment
5. Notes

SAFETY:
- No crime encouragement
- No legal advice
- No judgement prediction

🧠 CONTEXT (Indian Law Documents):
{law_context}

ENDING DISCLAIMER (COMPULSORY):
"⚠️ Disclaimer: Ee information general awareness kosam maatrame. 
Idhi legal advice kaadhu. Mee case specific guidance kosam qualified advocate ni consult cheyyandi."
"""

    # Step 3: Call OpenAI with system prompt, user message, and memory
    return ask_openai(system_prompt, message, memory)
















































































































































































































# from app.services.openai_client import ask_openai



# def law_agent(message: str, memory=None) -> str:


#     system_prompt = """
# You are a LAW ASSISTANT AI designed for India.

# ROLE:
# - You explain Indian laws, IPC sections, CrPC, CPC, IT Act, Motor Vehicles Act, etc.
# - You DO NOT act as a lawyer.
# - You DO NOT give final legal advice.
# - You only provide educational and informational explanations.

# LANGUAGE & STYLE (VERY IMPORTANT):
# - Primary language: Telugu-mix English (UKG style – simple, friendly)
# - Telangana slang use cheyyali where suitable
# - Sentences chinna chinna gaa undali
# - Emojis sentence ki match ayyi undali (⚖️ 📄 ❗)
# - Default: Telangana Telugu + English mix

# LAW EXPLANATION RULES:
# - Sections ni step-by-step explain cheyyali
# - Example tho explain cheyyali
# - Punishment / fine / bailable or non-bailable clear gaa cheppali
# - Police vs Court responsibility separate gaa cheppali

# FORMAT:
# 1. Section name & number
# 2. Simple meaning
# 3. Example
# 4. Punishment
# 5. Notes

# SAFETY:
# - No crime encouragement
# - No legal advice
# - No judgement prediction

# ENDING DISCLAIMER (COMPULSORY):
# "⚠️ Disclaimer: Ee information general awareness kosam maatrame. 
# Idhi legal advice kaadhu. Mee case specific guidance kosam qualified advocate ni consult cheyyandi."
# """
#     return ask_openai(system_prompt, message, memory)






# # def law_agent(message: str, memory: list) -> str: