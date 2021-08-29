from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/")
def home():
    return {"name" : "Hello World app", "version": "2.0.0"}

@app.get("/file/{filePath:path}")
def getFileByPath(filePath: str):
    return {'received' : filePath}