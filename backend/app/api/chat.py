from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.agent_router import run_agent

router = APIRouter()

class ChatRequest(BaseModel):
    chat_id: str
    message: str

@router.post("/chat")
def chat_endpoint(payload: ChatRequest):
    try:
        return run_agent(payload.chat_id, payload.message)
    except Exception as e:
        print("🔥 ERROR INSIDE /chat:", e)
        raise HTTPException(status_code=500, detail=str(e))












































































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
