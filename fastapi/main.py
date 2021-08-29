from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class CountryEnum(str, Enum):
    India = "India"
    China = "China"
    Russia = "Russia"

# model classes
class Employee(BaseModel):
    name: str
    age: int
    country: str

class EmployeeUpdateDto(BaseModel):
    name: Optional[str]
    age : Optional[int]
    country: Optional[str]

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

@app.get("/emps/by-id/self")
def self():
    return {'name' : 'Krishna', 'age' : 32, 'country' : 'russia'}
    
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
    
    empsTemp = []
    for empId in emps:
        if emps[empId]["name"] == name:
            empsTemp.append(emps[empId])
    return empsTemp

@app.get("/emps/by-country/{countryName}")
def empByCountryName(countryName: CountryEnum):
    empsTemp = []

    for empId in emps:
        if (emps[empId]["country"] == countryName.name):
            empsTemp.append(emps[empId])
    return empsTemp

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

    if(emp.country != None):
        persistedEmp["country"] = emp.country

    return {"id" : empId, "name" : persistedEmp["name"], "age": persistedEmp["age"], "country" : persistedEmp["country"]}

@app.delete("/emps/by-id/{empId}")
def deleteEmpById(empId: int = Path(None, description = "Enter valid employee id")):
    if(empId in emps):
        del emps[empId]
        return {"msg" : "Employee is deleted with given id " + str(empId)}
    else:
        return {"msg" : "Employee not exist with given id " + str(empId)}