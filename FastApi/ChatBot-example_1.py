from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat")
def chat(message: Message):
    user_input = message.user_input
    if "안녕" in user_input:
        response = "안녕하세요! 무엇을 도와드릴까요?"
    elif "이름" in user_input:
        response = "저는 FastAPI 챗봇입니다."
    elif "날씨" in user_input:
        response = "오늘의 날씨는 맑음입니다!"
    else:
        response = "잘 이해하지 못했어요. 다시 말씀해 주세요."
    return {"response": response}