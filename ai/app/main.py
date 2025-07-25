from fastapi import FastAPI
from app.api.routes import prompt
from app.api.sessions import session


app = FastAPI()

# app.include_router(voice.router, prefix="/voice")
# app.include_router(finance.router, prefix="/finance")
# app.include_router(group.router, prefix="/group")
app.include_router(session.router, prefix="/sessions")
app.include_router(prompt.router, prefix="/prompt")
