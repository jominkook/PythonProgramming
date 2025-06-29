# 예시 2: FastAPI + HTML 폼 챗봇
from fastapi import FastAPI,HTMLResponse
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def form():
    return """
    <form action="/chat" method="post">
        <input name="message" type="text">
        <input type="submit">
    </form>
    """