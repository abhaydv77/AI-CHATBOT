from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from chatbot import get_response
from collections import defaultdict
import time

app = FastAPI()

# CORS Protection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-chatbot-cve8.onrender.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

# Rate Limiting — per IP: 10 requests per minute
rate_limit_store = defaultdict(list)
RATE_LIMIT = 10
TIME_WINDOW = 60

def check_rate_limit(ip: str):
    now = time.time()
    timestamps = rate_limit_store[ip]
    rate_limit_store[ip] = [t for t in timestamps if now - t < TIME_WINDOW]
    if len(rate_limit_store[ip]) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Bhai thoda ruk ja! Zyada fast mat chal 🛑")
    rate_limit_store[ip].append(now)

# Input Validation
class MessageRequest(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def validate_message(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Message khali nahi ho sakta!")
        if len(v) > 500:
            raise ValueError("Message bahut lamba hai! 500 characters se kam rakho.")
        return v

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/chat")
async def chat(req: MessageRequest, request: Request):
    ip = request.client.host
    check_rate_limit(ip)
    reply = get_response(req.message)
    return {"reply": reply}

app.mount("/static", StaticFiles(directory="static"), name="static")
