from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# model classes
class Employee(BaseModel):
    name: str
    age: int

class EmployeeResponseDto(BaseModel):
    name: str
    age : int
    id: int

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32
    },
    2 : {
        "name" : "Ram",
        "age": 33
    },
    3 : {
        "name" : "Bomma",
        "age": 38
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
    
@app.post(
    "/emps",
    response_description="Employee created successfully",
    response_model = EmployeeResponseDto)
def createEmployee(emp: Employee):
    noOfEmps = len(emps)
    newId = noOfEmps + 1
    emps[newId] = emp
    return {"id" : newId, "name" : emp.name, "age": emp.age}
