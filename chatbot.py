from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

chat_history = [
    SystemMessage(content="you're a rapper who talks in rhyme. Always respond with bars, keep it funky and rhythmic.")
]

def get_response(user_message: str) -> str:
    chat_history.append(HumanMessage(content=user_message))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    return response.content
