# app/agents/decide_agent.py

def decide_agent(message: str) -> str:
    msg = message.lower()

    # 📰 PRESS priority
    if any(word in msg for word in [
        "news", "article", "press", "media",
        "headline", "journalist", "report"
    ]):
        return "PRESS"

    # 🚓 POLICE priority
    if any(word in msg for word in [
        "fir", "complaint", "investigation",
        "arrest", "accused", "police"
    ]):
        return "POLICE"

    # ⚖️ default LAW
    return "LAW"
