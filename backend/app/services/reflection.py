from app.services.openai_client import ask_openai


REFLECTION_PROMPT = """
You are an AI quality reviewer.

Task:
- Review the assistant's answer
- Check for factual uncertainty
- Identify assumptions
- Assess clarity and safety

Return STRICT JSON with:
{
  "confidence": number (0-100),
  "notes": "short explanation of confidence score"
}

Rules:
- Be conservative
- If unsure, reduce confidence
- Do NOT rewrite the answer
"""


def reflect(answer: str, memory: list) -> dict:
    """
    Reflection Agent: Analyzes response quality and assigns confidence score.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate the answer to ensure it's not empty
    2. Send answer to OpenAI with reflection prompt for quality assessment
    3. Parse the JSON response containing confidence and notes
    4. Return quality assessment with fallback for parsing errors
    
    QUALITY ASSESSMENT CRITERIA:
    - Factual accuracy vs assumptions
    - Presence of uncertainty or speculation
    - Clarity and educational value
    - Safety and disclaimer compliance
    - Appropriate scope and boundaries
    
    CONFIDENCE SCORING:
    - 80-100: High quality, factual, clear disclaimers
    - 60-79: Good but some uncertainty or assumptions
    - 40-59: Moderate quality with notable concerns
    - 0-39: Low quality, risky, or unclear
    
    Args:
        answer (str): The AI response to evaluate
        memory (list): Conversation history (currently unused but available)
        
    Returns:
        dict: Quality assessment containing:
            - confidence: Score 0-100 indicating response quality
            - notes: Brief explanation of the confidence score
            
    Edge cases handled:
    - Empty answer: Returns low confidence (40)
    - JSON parsing errors: Returns moderate confidence (60)
    - OpenAI API errors: Caught by ask_openai, returns fallback
    - Invalid confidence values: Clamped to 0-100 range
    """
    try:
        # Edge case: Validate answer
        if not answer or not isinstance(answer, str) or not answer.strip():
            return {
                "confidence": 40,
                "notes": "Empty or invalid answer provided"
            }
        
        # Step 1: Call OpenAI to review answer quality
        review = ask_openai(
            REFLECTION_PROMPT,
            answer,
            memory=[]
        )

        # Step 2: Parse JSON response
        try:
            import json
            result = json.loads(review)
            
            # Edge case: Validate and clamp confidence score
            confidence = result.get("confidence", 60)
            if not isinstance(confidence, (int, float)):
                confidence = 60
            confidence = max(0, min(100, confidence))  # Clamp to 0-100
            
            # Edge case: Validate notes field
            notes = result.get("notes", "Quality assessment completed")
            if not isinstance(notes, str):
                notes = "Quality assessment completed"
            
            return {
                "confidence": confidence,
                "notes": notes
            }
            
        except Exception as parse_error:
            # Edge case: JSON parsing failed - return moderate confidence
            print(f"⚠️ Reflection parsing error: {parse_error}")
            return {
                "confidence": 60,
                "notes": "Automatic confidence assigned due to parsing issue"
            }
            
    except Exception as e:
        # Edge case: Unexpected error - return moderate confidence
        print(f"🔥 Reflection error: {e}")
        return {
            "confidence": 60,
            "notes": "Automatic confidence assigned due to system error"
        }
