from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# model classes
class Employee(BaseModel):
    name: str
    age: int
    country: str

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32,
        "country": "India"
    },
    2 : {
        "name" : "Ram",
        "age": 33,
        "country": "China"
    },
    3 : {
        "name" : "Bomma",
        "age": 38,
        "country": "China"
    }
}

# Create home endpoint
@app.get("/")
def home():
    return {"name" : "Hello World app", "version": "2.0.0"}

# Employees REST APIs
@app.get("/emps")
def allEmployees():
    return emps

@app.post("/emps", status_code=201)
def createEmployee(emp: Employee):
    noOfEmps = len(emps)
    newId = noOfEmps + 1
    emps[newId] = emp
    return {"id" : newId, "name" : emp.name, "age": emp.age, "country": emp.country}
