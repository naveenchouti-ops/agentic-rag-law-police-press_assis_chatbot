from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from dotenv import load_dotenv
import os

load_dotenv()



app = FastAPI(
    title="Law AI Backend",
    debug=True
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running 🚀"}

app.include_router(chat_router)
