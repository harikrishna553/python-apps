from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32
    }
}

class Employee(BaseModel):
    name: str
    age : int

@app.get("/emps")
def allEmployees():
    return emps

@app.post("/emps")
def createEmployee(
    emp: Employee = Body(
        ..., 
        example = {"name" : "Krishna", "age": 31}
    )
):
    noOfEmps = len(emps)
    newId = noOfEmps + 1
    emps[newId] = dict(emp)

    return {
        "id" : newId, 
        "name" : emps[newId]['name'], 
        "age": emps[newId]['age']
        }