from fastapi import FastAPI, Header
from typing import Optional

app = FastAPI()

@app.get("/demo")
def headers_demo(
    user_agent: Optional[str] = Header(None),
    content_encoding: Optional[str] = Header(None)):
    return {"user_agent" : user_agent, "content_encoding" : content_encoding}