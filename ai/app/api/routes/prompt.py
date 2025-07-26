from fastapi import APIRouter
from pydantic import BaseModel
import requests
from ..sessions.session import create_or_get_session, user_sessions
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
    app_name: str
    new_message: NewMessage
    streaming: bool

@router.post("/ask")
def accept_prompt(req: PromptRequest):
    # Get or create session_id
    session_id = user_sessions.get((req.app_name,req.user_id))
    if not session_id:
        session_id = create_or_get_session(req.app_name,req.user_id)
        session_id=str(session_id)
    payload = {
        "app_name": req.app_name,
        "user_id": req.user_id,
        "session_id": session_id,
        "new_message": req.new_message.dict(),
        "streaming": req.streaming
    }
    PORT_NUMBER = 8001
    if req.app_name == "chart_analyzer_agent":
        PORT_NUMBER = 8002
    elif req.app_name == "wealth_manager_agent":
        PORT_NUMBER = 8003
    elif req.app_name == "loan_insurance_agent":
        PORT_NUMBER = 8004
    elif req.app_name == "net_worth_tracker_agent":
        PORT_NUMBER = 8005
    elif req.app_name == "affordability_analysis_agent":
        PORT_NUMBER = 8006
    endpoint = "run_sse" if req.streaming else "run"
    url = f"{BASE_URL}:{PORT_NUMBER}/{endpoint}"
    print(url)
    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return {"error": "Failed to process the request", "details": str(e)}
    print(resp)

