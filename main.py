from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from chatbot import get_response

app = FastAPI()

class MessageRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/chat")
def chat(req: MessageRequest):
    reply = get_response(req.message)
    return {"reply": reply}

app.mount("/static", StaticFiles(directory="static"), name="static")
