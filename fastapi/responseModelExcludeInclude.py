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
    country: str = 'India'
    tax: float = 30.5

emp1 = Employee(name= "Krishna", age = 32, country = "India", tax = 20)
emp2 = Employee(name= "Ram", age = 42, country = "China", tax = 35)
emp3 = Employee(name= "Sailu", age = 33)

employees = {1 : emp1, 2 : emp2, 3 : emp3}

@app.get("/emps/by-id-ex1/{empId}", response_model = Employee, response_model_include ={'name', 'country'})
def empById(empId: int = Path(None, description = "Enter valid employee id", gt = 0, lt = 4)):
    if(empId in employees):
        return employees[empId]
    else:
        raise Exception("Employee not exist with given id " + str(empId))

@app.get("/emps/by-id-ex2/{empId}", response_model = Employee, response_model_exclude={'age','tax'})
def empById(empId: int = Path(None, description = "Enter valid employee id", gt = 0, lt = 4)):
    if(empId in employees):
        return employees[empId]
    else:
        raise Exception("Employee not exist with given id " + str(empId))