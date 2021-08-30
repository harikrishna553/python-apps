from fastapi import FastAPI, Path, Query
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

class Address(BaseModel):
    street: str
    city: str

@app.get("/emps")
def allEmployees():
    return emps

@app.post("/emps")
def createEmployee(emp: Employee, address: Address):
    noOfEmps = len(emps)
    newId = noOfEmps + 1
    emps[newId] = dict(emp)
    emps[newId]['address'] = dict(address)

    return {
        "id" : newId, 
        "name" : emps[newId]['name'], 
        "age": emps[newId]['age'],
        "address" : emps[newId]['address']
        }