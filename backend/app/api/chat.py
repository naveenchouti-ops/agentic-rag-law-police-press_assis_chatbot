from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.agent_router import run_agent

router = APIRouter()

class ChatRequest(BaseModel):
    chat_id: str
    message: str

@router.post("/chat")
def chat_endpoint(payload: ChatRequest):
    """
    Main chat endpoint for handling user messages.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Receive and validate the chat request payload via Pydantic
    2. Extract chat_id and message from the request
    3. Validate that both fields are non-empty strings
    4. Route the request to the agent_router for processing
    5. Return the agent's response to the client
    6. Handle any errors and return appropriate HTTP status codes
    
    REQUEST VALIDATION:
    - chat_id: Required, must be non-empty string (session identifier)
    - message: Required, must be non-empty string (user query)
    
    RESPONSE FORMAT:
    - Returns dict from agent_router containing:
      - mode: "single" or "voting"
      - reply/final_answer: AI response text
      - agent_used/winner: Which agent responded
      - confidence: Quality score
      - Additional metadata
    
    Args:
        payload (ChatRequest): Request body with chat_id and message
        
    Returns:
        dict: Agent response with answer and metadata
        
    Raises:
        HTTPException: 400 for invalid input, 500 for processing errors
        
    Edge cases handled:
    - Empty chat_id: Returns 400 Bad Request
    - Empty message: Returns 400 Bad Request
    - Processing errors: Returns 500 Internal Server Error with details
    - Invalid payload format: Caught by Pydantic validation
    """
    try:
        # Edge case: Validate chat_id
        if not payload.chat_id or not payload.chat_id.strip():
            raise HTTPException(
                status_code=400,
                detail="chat_id is required and must not be empty"
            )
        
        # Edge case: Validate message
        if not payload.message or not payload.message.strip():
            raise HTTPException(
                status_code=400,
                detail="message is required and must not be empty"
            )
        
        # Route to agent system for processing
        return run_agent(payload.chat_id, payload.message)
        
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        # Edge case: Unexpected errors during processing
        print("🔥 ERROR INSIDE /chat:", e)
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )












































































# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.agents.agent_router import run_agent

# router = APIRouter()

# class ChatRequest(BaseModel):
#     chat_id: str
#     message: str

# @router.post("/chat")
# def chat_endpoint(payload: ChatRequest):
#     return run_agent(payload.chat_id, payload.message)








































# # from fastapi import APIRouter
# # from app.models.schemas import ChatRequest, ChatResponse
# # from app.agents.agent_router import run_agent

# # router = APIRouter()

# # # @router.post("/chat", response_model=ChatResponse)
# # # def chat_endpoint(payload: ChatRequest):
# # #     reply = run_agent(payload.message)
# # #     return ChatResponse(reply=reply)

# # @router.post("/chat")
# # def chat_endpoint(payload: dict):
# #     result = run_agent(
# #         chat_id=payload.get("chat_id", "default"),
# #         message=payload["message"]
# #     )
# #     return result
