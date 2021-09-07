from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get(
    "/emps", 
    tags=["employees"], 
    summary="Get employees", 
    description = "Return all the active employees"
)
def emps():
    return {"msg": "Return all employees"}

@app.get(
    "/items", 
    tags=["items"],
    summary = "Get items", 
    description = "Return all the active items")
def items():
    return {"msg": "Return all items"}

@app.get(
    "/items/{itemId}", 
    tags=["items"], 
    summary = "Get the item", 
    description = "Get the item details by its id")
def itemById():
    return {"msg": "Return item by id"}