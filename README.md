# 🎤 AI Rapper Chatbot

A chatbot that replies to everything in rap bars. You talk, it spits fire.

Built with Python, LangChain, Groq API, and FastAPI.

---

## What it does

You type something, the bot responds in rhymes like a rapper. That's it. Simple but fun.

---

## Setup

1. Clone the repo
```bash
git clone https://github.com/abhaydv77/AI-CHATBOT.git
cd AI-CHATBOT
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your Groq API key — create a `.env` file:
```
GROQ_API_KEY=your_key_here
```
Get a free key at https://console.groq.com

4. Run it
```bash
uvicorn main:app --reload
```

Open http://localhost:8000 and start dropping bars 🎙️

---
## 🌐 Live Demo

👉 https://ai-chatbot-cve8.onrender.com/


## A note from me

The core AI chatbot logic — connecting to the Groq API, managing chat history, using LangChain — I built that myself.

For wrapping it into a web app with FastAPI, I took help from AI since I was still learning how backends work.

The frontend (HTML/CSS/JS) is fully AI generated. I didn't write that part, just told it what I wanted and it built it.

Honestly, I think that's fine. Knowing *what* to build and *how to put it together* matters more than writing every single line yourself. This project taught me a lot about how APIs, backends, and frontends connect with each other.

Also — the bot is still new so it doesn't always respond perfectly. I'm planning to train it more and improve it over time.

**Future plan:** Connect it to a database so it can actually remember conversations instead of forgetting everything on every restart.

— Abhay
