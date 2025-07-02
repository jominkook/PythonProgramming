from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "YOUR_OPENAI_API_KEY"

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": req.message}]
    )
    answer = response.choices[0].message.content
    return {"response": answer}