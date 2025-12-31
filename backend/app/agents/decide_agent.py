# app/agents/decide_agent.py

def decide_agent(message: str) -> str:
    """
    Analyze user message and decide which specialized agent should handle it.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate that the message is a non-empty string
    2. Convert message to lowercase for case-insensitive keyword matching
    3. Check for PRESS-related keywords (news, media, journalism)
    4. Check for POLICE-related keywords (FIR, investigation, arrest)
    5. Default to LAW agent for general legal queries
    6. Return the agent name as a string constant
    
    DECISION PRIORITY:
    - PRESS agent: For news, articles, media, and journalism queries
    - POLICE agent: For FIR, complaints, investigations, and arrest procedures  
    - LAW agent: Default for legal explanations (IPC, CrPC, etc.)
    
    Args:
        message (str): The user's input message to analyze
        
    Returns:
        str: Agent name - "PRESS", "POLICE", or "LAW"
        
    Edge cases handled:
    - Empty or None message: Returns "LAW" (safe default)
    - Non-string message: Returns "LAW" (safe default)
    - Multiple matching keywords: Uses priority order (PRESS > POLICE > LAW)
    """
    # Edge case: Validate message
    if not message or not isinstance(message, str) or not message.strip():
        return "LAW"  # Safe default
    
    # Step 1: Normalize message for keyword matching
    msg = message.lower().strip()

    # Step 2: Check for PRESS priority keywords (highest priority for news/media)
    if any(word in msg for word in [
        "news", "article", "press", "media",
        "headline", "journalist", "report"
    ]):
        return "PRESS"

    # Step 3: Check for POLICE priority keywords (second priority for procedural queries)
    if any(word in msg for word in [
        "fir", "complaint", "investigation",
        "arrest", "accused", "police"
    ]):
        return "POLICE"

    # Step 4: Default to LAW agent for general legal queries
    return "LAW"
