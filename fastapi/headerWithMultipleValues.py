from fastapi import FastAPI, Header
from typing import Optional, List

app = FastAPI()

@app.get("/demo")
def headers_demo(
    x_my_keys: Optional[List[str]] = Header(None)):
    return {"x_my_keys" : x_my_keys}