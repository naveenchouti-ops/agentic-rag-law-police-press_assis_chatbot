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
    review = ask_openai(
        REFLECTION_PROMPT,
        answer,
        memory=[]
    )

    # Fallback safety
    try:
        import json
        return json.loads(review)
    except Exception:
        return {
            "confidence": 60,
            "notes": "Automatic confidence assigned due to parsing issue"
        }
