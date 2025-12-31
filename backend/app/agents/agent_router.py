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
    Central agent router - main entry point for all chat requests.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate input parameters (chat_id, message, mode)
    2. Check the mode parameter to determine execution strategy
    3. Route to voting mode for multi-agent evaluation (advanced)
    4. Route to single mode for fast production responses (default)
    5. Return structured response with agent info and reply
    
    MODES:
    - "single": Fast mode - one agent responds based on query analysis
    - "voting": Advanced mode - all agents respond, judge picks best answer
    
    Args:
        chat_id (str): Unique identifier for the conversation session
        message (str): User's input question or query
        mode (str, optional): Execution mode. Defaults to "single".
        
    Returns:
        dict: Response object containing:
            - mode: Execution mode used
            - reply/final_answer: AI's response text
            - agent_used/winner: Which agent provided the answer
            - confidence: Quality score (0-100)
            - Additional metadata based on mode
            
    Edge cases handled:
    - Invalid mode: Defaults to "single" mode
    - Empty message: Handled by downstream functions
    - None chat_id: Handled by downstream functions
    """
    # Edge case: Validate and normalize mode parameter
    if not mode or not isinstance(mode, str) or mode.lower() not in ["single", "voting"]:
        mode = "single"  # Safe default
    
    mode = mode.lower()
    
    # Route to appropriate execution strategy
    if mode == "voting":
        return run_agent_with_voting(chat_id, message)

    return run_single_agent(chat_id, message)


# =====================================================
# 1️⃣ SINGLE AGENT MODE (FAST / PRODUCTION DEFAULT)
# =====================================================
def run_single_agent(chat_id: str, message: str) -> dict:
    """
    Execute single-agent mode: fast, efficient response from one specialized agent.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate input parameters
    2. Load conversation history from memory for context
    3. Save the user's message to memory before processing
    4. Analyze the message to decide which agent should respond
    5. Route to the appropriate specialized agent (LAW/POLICE/PRESS)
    6. Run reflection analysis to assess response quality
    7. Save the assistant's reply to memory for future context
    8. Return structured response with metadata
    
    WORKFLOW:
    User Message → Memory → Decide Agent → Specialized Agent → Reflection → Save → Return
    
    Args:
        chat_id (str): Unique conversation identifier
        message (str): User's question or input
        
    Returns:
        dict: Response containing:
            - mode: "single"
            - agent_used: Which agent responded (LAW/POLICE/PRESS)
            - reply: The AI's answer text
            - confidence: Quality score from reflection (0-100)
            - notes: Additional context about the response
            
    Edge cases handled:
    - Empty message: Returns error response
    - Invalid chat_id: Creates new conversation
    - Reflection failure: Uses default confidence score
    - Agent execution errors: Caught and handled
    """
    try:
        # Edge case: Validate message
        if not message or not isinstance(message, str) or not message.strip():
            return {
                "mode": "single",
                "agent_used": "NONE",
                "reply": "⚠️ Please provide a valid message.",
                "confidence": 0,
                "notes": "Invalid input"
            }
        
        # Step 1: Load conversation memory for context
        memory = get_memory(chat_id)

        # Step 2: Save user message FIRST to maintain conversation flow
        add_message(chat_id, "user", message)

        # Step 3: Decide which agent should handle this query
        agent = decide_agent(message)

        # Step 4: Route to appropriate specialized agent
        if agent == "PRESS":
            reply = press_agent(message, memory)
        elif agent == "POLICE":
            reply = police_agent(message, memory)
        else:
            reply = law_agent(message, memory)

        # Step 5: Run reflection to assess response quality
        try:
            reflection = reflect(reply, memory)
        except Exception:
            # Fallback if reflection fails
            reflection = {
                "confidence": 0.7,
                "notes": "Reflection skipped due to internal safety."
            }

        # Step 6: Save assistant reply for conversation continuity
        add_message(chat_id, "assistant", reply)

        # Step 7: Return structured response
        return {
            "mode": "single",
            "agent_used": agent,
            "reply": reply,
            "confidence": reflection.get("confidence", 0.7),
            "notes": reflection.get("notes", "")
        }
        
    except Exception as e:
        # Edge case: Handle unexpected errors
        print(f"🔥 ERROR in run_single_agent: {e}")
        return {
            "mode": "single",
            "agent_used": "ERROR",
            "reply": "⚠️ An error occurred while processing your request. Please try again.",
            "confidence": 0,
            "notes": "System error"
        }


# =====================================================
# 2️⃣ MULTI-AGENT VOTING MODE (ADVANCED / AUDIT)
# =====================================================
def run_agent_with_voting(chat_id: str, message: str) -> dict:
    """
    Execute voting mode: all agents respond, judge selects the best answer.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate input parameters
    2. Load conversation memory for context
    3. Save user message before processing
    4. Execute all three agents in parallel to get diverse perspectives
    5. Send all answers to judge agent for evaluation
    6. Judge analyzes quality, safety, and accuracy of each answer
    7. Select the winning answer based on judge's decision
    8. Save only the final winning answer to memory
    9. Return comprehensive response with all answers and verdict
    
    WORKFLOW:
    User Message → Memory → [LAW + POLICE + PRESS] → Judge → Winner → Save → Return
    
    USE CASES:
    - Quality assurance and auditing
    - Critical queries requiring highest accuracy
    - Compliance and safety verification
    - Development and testing environments
    
    Args:
        chat_id (str): Unique conversation identifier
        message (str): User's question or input
        
    Returns:
        dict: Response containing:
            - mode: "voting"
            - final_answer: The winning agent's response
            - winner: Which agent won (law_agent/police_agent/press_agent)
            - confidence: Judge's confidence in the selection
            - reason: Judge's explanation for the choice
            - all_answers: All three agents' responses (for debugging)
            
    Edge cases handled:
    - Empty message: Returns error response
    - Judge failure: Falls back to law_agent answer
    - Invalid winner selection: Uses law_agent as default
    - Agent execution errors: Caught and handled
    """
    try:
        # Edge case: Validate message
        if not message or not isinstance(message, str) or not message.strip():
            return {
                "mode": "voting",
                "final_answer": "⚠️ Please provide a valid message.",
                "winner": "NONE",
                "confidence": 0,
                "reason": "Invalid input",
                "all_answers": {}
            }
        
        # Step 1: Load conversation memory
        memory = get_memory(chat_id)

        # Step 2: Save user message for context
        add_message(chat_id, "user", message)

        # Step 3: Run all agents independently to get diverse perspectives
        answers = {
            "law_agent": law_agent(message, memory),
            "police_agent": police_agent(message, memory),
            "press_agent": press_agent(message, memory),
        }

        # Step 4: Judge evaluates all answers for quality and safety
        verdict = judge(message, answers)

        # Step 5: Select winning answer (with safe fallback)
        winner_key = verdict.get("winner", "law_agent")
        
        # Edge case: Ensure winner_key is valid
        if winner_key not in answers:
            winner_key = "law_agent"
            
        final_answer = answers.get(winner_key, answers["law_agent"])

        # Step 6: Save ONLY the final winning answer to maintain clean memory
        add_message(chat_id, "assistant", final_answer)

        # Step 7: Return comprehensive response with verdict details
        return {
            "mode": "voting",
            "final_answer": final_answer,
            "winner": winner_key,
            "confidence": verdict.get("confidence", 0.6),
            "reason": verdict.get("reason", ""),
            "all_answers": answers  # dev/debug only
        }
        
    except Exception as e:
        # Edge case: Handle unexpected errors
        print(f"🔥 ERROR in run_agent_with_voting: {e}")
        return {
            "mode": "voting",
            "final_answer": "⚠️ An error occurred while processing your request. Please try again.",
            "winner": "ERROR",
            "confidence": 0,
            "reason": "System error",
            "all_answers": {}
        }
