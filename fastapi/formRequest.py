from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/register-me", status_code=201)
async def login(
    username: str = Form(...), 
    password: str = Form(...),
    country: str = Form(...)):
    return {"username": username, "country": country}