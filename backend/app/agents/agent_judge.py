from app.services.openai_client import ask_openai


JUDGE_PROMPT = """
You are an expert AI judge.

You will receive:
- A user question
- Multiple agent answers (LAW, POLICE, PRESS)

Your task:
1. Compare all answers
2. Identify inaccuracies or risks
3. Decide which answer is BEST for the user
4. Give a confidence score (0–100)

Rules:
- Prefer safety over completeness
- Prefer educational tone
- Avoid legal advice or verdicts
- Be conservative

Return STRICT JSON only in this format:
{
  "winner": "law_agent | police_agent | press_agent",
  "confidence": number,
  "reason": "short explanation"
}
"""


def judge(user_message: str, answers: dict) -> dict:
    """
    Judge Agent: Evaluates multiple agent responses and selects the best answer.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate inputs (user_message and answers dictionary)
    2. Build a combined input showing the question and all agent responses
    3. Send to OpenAI with judge prompt to evaluate quality and safety
    4. Parse the JSON response containing winner, confidence, and reason
    5. Return the verdict with fallback handling for parsing errors
    
    EVALUATION CRITERIA:
    - Safety and accuracy (highest priority)
    - Educational tone over authoritative claims
    - Factual grounding and disclaimer presence
    - Appropriate scope (no overreach into legal advice)
    - Clarity and helpfulness for user
    
    Args:
        user_message (str): The original user question
        answers (dict): Dictionary with keys 'law_agent', 'police_agent', 'press_agent'
                       and their corresponding response strings
        
    Returns:
        dict: Verdict containing:
            - winner: Key of winning agent (e.g., "law_agent")
            - confidence: Score 0-100 indicating judge's certainty
            - reason: Brief explanation of the decision
            
    Edge cases handled:
    - Empty user_message: Returns fallback to law_agent
    - Missing answers: Returns fallback to law_agent
    - Invalid answers dict: Returns fallback to law_agent
    - JSON parsing errors: Returns fallback verdict
    - OpenAI API errors: Caught by ask_openai, returns fallback
    """
    try:
        # Edge case: Validate user_message
        if not user_message or not isinstance(user_message, str) or not user_message.strip():
            return {
                "winner": "law_agent",
                "confidence": 50,
                "reason": "Invalid user message - defaulting to law agent"
            }
        
        # Edge case: Validate answers dictionary
        if not answers or not isinstance(answers, dict):
            return {
                "winner": "law_agent",
                "confidence": 50,
                "reason": "Invalid answers provided - defaulting to law agent"
            }
        
        # Step 1: Build combined input with all agent responses
        combined_input = f"""
USER QUESTION:
{user_message}

LAW AGENT ANSWER:
{answers.get("law_agent", "No response")}

POLICE AGENT ANSWER:
{answers.get("police_agent", "No response")}

PRESS AGENT ANSWER:
{answers.get("press_agent", "No response")}
"""

        # Step 2: Call OpenAI to evaluate and select best answer
        result = ask_openai(
            system_prompt=JUDGE_PROMPT,
            user_message=combined_input,
            memory=[]
        )

        # Step 3: Parse JSON response
        try:
            import json
            verdict = json.loads(result)
            
            # Edge case: Validate verdict structure
            if "winner" not in verdict or verdict["winner"] not in ["law_agent", "police_agent", "press_agent"]:
                verdict["winner"] = "law_agent"
            
            if "confidence" not in verdict or not isinstance(verdict.get("confidence"), (int, float)):
                verdict["confidence"] = 60
            
            if "reason" not in verdict:
                verdict["reason"] = "Fallback decision"
                
            return verdict
            
        except Exception as parse_error:
            # Edge case: JSON parsing failed - return safe fallback
            print(f"⚠️ Judge parsing error: {parse_error}")
            return {
                "winner": "law_agent",
                "confidence": 60,
                "reason": "Fallback decision due to parsing issue"
            }
            
    except Exception as e:
        # Edge case: Unexpected error - return safe fallback
        print(f"🔥 Judge error: {e}")
        return {
            "winner": "law_agent",
            "confidence": 50,
            "reason": "Fallback decision due to system error"
        }
