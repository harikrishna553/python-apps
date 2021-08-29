from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {'name' : 'Hello World app', 'version': '2.0.0'}

@app.get("/emps")
def emps( sortBy: str, pageNum : int = 1, pageSize : Optional[int] = None):
    return {'received' : {'sortBy' : sortBy, 'pageNum' : pageNum, 'pageSize': pageSize}}