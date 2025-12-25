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
    combined_input = f"""
USER QUESTION:
{user_message}

LAW AGENT ANSWER:
{answers.get("law_agent")}

POLICE AGENT ANSWER:
{answers.get("police_agent")}

PRESS AGENT ANSWER:
{answers.get("press_agent")}
"""

    result = ask_openai(
        system_prompt=JUDGE_PROMPT,
        user_message=combined_input,
        memory=[]
    )

    try:
        import json
        return json.loads(result)
    except Exception:
        return {
            "winner": "law_agent",
            "confidence": 60,
            "reason": "Fallback decision due to parsing issue"
        }
