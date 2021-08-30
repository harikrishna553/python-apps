from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32,
        "address": {
            "street" : "Chowdeswari",
            "city" : "Bangalore"
        }
    }
}

class Employee(BaseModel):
    name: str
    age : int

@app.get("/emps")
def allEmployees():
    return emps

@app.post("/emps")
def createEmployee(emp: Employee, street: str = Body(...), city: str = Body(...)):
    noOfEmps = len(emps)
    newId = noOfEmps + 1
    emps[newId] = dict(emp)

    address = {"street" : street, "city" : city}
    emps[newId]['address'] = address

    return {
        "id" : newId, 
        "name" : emps[newId]['name'], 
        "age": emps[newId]['age'],
        "address" : emps[newId]['address']
        }