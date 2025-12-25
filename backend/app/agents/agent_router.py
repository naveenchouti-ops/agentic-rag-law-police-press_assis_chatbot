from app.agents.agent_law import law_agent
from app.agents.agent_police import police_agent
from app.agents.agent_press import press_agent
from app.agents.decide_agent import decide_agent
from app.agents.agent_judge import judge

from app.services.memory_manager import get_memory, add_message
from app.services.reflection import reflect


# =====================================================
# 🚀 MAIN ENTRY POINT (frontend calls ONLY this)
# mode = "single" | "voting"
# =====================================================
def run_agent(chat_id: str, message: str, mode: str = "single") -> dict:
    """
    Central agent router.
    Frontend must call ONLY this function.
    """
    if mode == "voting":
        return run_agent_with_voting(chat_id, message)

    return run_single_agent(chat_id, message)


# =====================================================
# 1️⃣ SINGLE AGENT MODE (FAST / PRODUCTION DEFAULT)
# =====================================================
def run_single_agent(chat_id: str, message: str) -> dict:
    # 🧠 Load conversation memory
    memory = get_memory(chat_id)

    # 🧠 Save user message FIRST
    add_message(chat_id, "user", message)

    # 🚦 Decide which agent should answer
    agent = decide_agent(message)

    # 🤖 Call selected agent
    if agent == "PRESS":
        reply = press_agent(message)
    elif agent == "POLICE":
        reply = police_agent(message)
    else:
        reply = law_agent(message)

    # 🪞 Reflection (safe wrapper)
    try:
        reflection = reflect(reply, memory)
    except Exception:
        reflection = {
            "confidence": 0.7,
            "notes": "Reflection skipped due to internal safety."
        }

    # 🧠 Save assistant reply
    add_message(chat_id, "assistant", reply)

    return {
        "mode": "single",
        "agent_used": agent,
        "reply": reply,
        "confidence": reflection.get("confidence", 0.7),
        "notes": reflection.get("notes", "")
    }


# =====================================================
# 2️⃣ MULTI-AGENT VOTING MODE (ADVANCED / AUDIT)
# =====================================================
def run_agent_with_voting(chat_id: str, message: str) -> dict:
    # 🧠 Load memory
    memory = get_memory(chat_id)

    # 🧠 Save user message
    add_message(chat_id, "user", message)

    # 🤖 Run all agents independently
    answers = {
        "law_agent": law_agent(message),
        "police_agent": police_agent(message),
        "press_agent": press_agent(message),
    }

    # ⚖️ Judge decides best answer
    verdict = judge(message, answers)

    winner_key = verdict.get("winner", "law_agent")
    final_answer = answers.get(winner_key, answers["law_agent"])

    # 🧠 Save ONLY final answer
    add_message(chat_id, "assistant", final_answer)

    return {
        "mode": "voting",
        "final_answer": final_answer,
        "winner": winner_key,
        "confidence": verdict.get("confidence", 0.6),
        "reason": verdict.get("reason", ""),
        "all_answers": answers  # dev/debug only
    }
