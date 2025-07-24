from fastapi import APIRouter
from pydantic import BaseModel
import requests
from app.api.sessions.session import user_sessions,create_or_get_session
from uuid import uuid4
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

router = APIRouter()

class MessagePart(BaseModel):
    text: str

class NewMessage(BaseModel):
    role: str
    parts: list[MessagePart]

class PromptRequest(BaseModel):
    user_id: str
    new_message: NewMessage
    streaming: bool

@router.post("/financial_analyzer")
def accept_prompt(req: PromptRequest):
    # Get or create session_id
    session_id = user_sessions.get(req.user_id)
    if not session_id:
        session_id = create_or_get_session(req.user_id)
    payload = {
        "app_name": "financial_news_analyzer",
        "user_id": req.user_id,
        "session_id": session_id,
        "new_message": req.new_message.dict(),
        "streaming": req.streaming
    }
    endpoint = "run_sse" if req.streaming else "run"
    url = f"{BASE_URL}/{endpoint}"
    resp = requests.post(url, json=payload)
    return resp.json()