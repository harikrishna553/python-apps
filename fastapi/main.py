from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# model classes
class Employee(BaseModel):
    name: str
    age: int

class EmployeeUpdateDto(BaseModel):
    name: Optional[str]
    age : Optional[int]

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32
    },
    2 : {
        "name" : "Ram",
        "age": 33
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

@app.get("/emps/by-id/{empId}")
def empById(empId: int = Path(None, description = "Enter valid employee id", gt = 0, lt = 3)):
    if(empId in emps):
        return emps[empId]
    else:
        raise Exception("Employee not exist with given id " + str(empId))

@app.get("/emps/by-name")
def empByName(name: Optional[str] = None):
    if name == None:
        return {"message" : "no input provided"}
    for empId in emps:
        if emps[empId]["name"] == name:
            return emps[empId]
    return {"message" : "Not found"}

@app.post("/emps")
def createEmployee(emp: Employee):
    noOfEmps = len(emps)
    newId = noOfEmps + 1
    emps[newId] = emp
    return {"id" : newId, "name" : emp.name, "age": emp.age}

@app.put("/emps/by-id/{empId}")
def updateEmployee(empId : int, emp: EmployeeUpdateDto):
    if(empId not in emps):
        return {"message" : "Not found"}
    
    persistedEmp = emps[empId]

    if(emp.name != None):
        persistedEmp["name"] = emp.name
    
    if(emp.age != None):
        persistedEmp["age"] = emp.age

    return {"id" : empId, "name" : persistedEmp["name"], "age": persistedEmp["age"]}

@app.delete("/emps/by-id/{empId}")
def deleteEmpById(empId: int = Path(None, description = "Enter valid employee id")):
    if(empId in emps):
        del emps[empId]
        return {"msg" : "Employee is deleted with given id " + str(empId)}
    else:
        return {"msg" : "Employee not exist with given id " + str(empId)}