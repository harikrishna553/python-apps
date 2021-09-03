from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/emps", tags=["employees"])
def emps():
    return {"msg": "Return all employees"}

@app.get("/items", tags=["items"])
def items():
    return {"msg": "Return all items"}

@app.get("/items/{itemId}", tags=["items"])
def productInfo():
    return {"msg": "Return item by id"}