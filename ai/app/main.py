from fastapi import FastAPI
from app.api.routes import voice, finance, group

app = FastAPI()

app.include_router(voice.router, prefix="/voice")
app.include_router(finance.router, prefix="/finance")
app.include_router(group.router, prefix="/group")