from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32,
        "gender" : 'M'
    },
    2 : {
        "name" : "Ram",
        "age": 33,
        "gender" : 'F'
    },
    3 : {
        "name" : "Bomma",
        "age": 38,
        "gender" : 'M'
    }
}

class EmployeeUpdateDto(BaseModel):
    name: str
    age : int

@app.get("/emps")
def allEmployees():
    return emps

@app.put("/emps/by-id/{empId}")
def updateEmployee(empId : int, emp: EmployeeUpdateDto, gender: Optional[str] = None):
    if(empId not in emps):
        return {"message" : "Not found"}
    
    persistedEmp = emps[empId]

    if(emp.name != None):
        persistedEmp["name"] = emp.name
    
    if(emp.age != None):
        persistedEmp["age"] = emp.age

    persistedEmp["gender"] = gender

    if(gender == None):
        persistedEmp["gender"] = 'M'
    
    return {
        "id" : empId, 
        "name" : persistedEmp["name"], 
        "age": persistedEmp["age"], 
        "gender" : persistedEmp["gender"]
        }