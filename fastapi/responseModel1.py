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

emp1 = Employee(name= "Krishna", age = 32, country = "India")
emp2 = Employee(name= "Ram", age = 42, country = "India")
emp3 = Employee(name= "Sailu", age = 33, country = "India")

employees = {1 : emp1, 2 : emp2, 3 : emp3}

@app.get("/emps/by-id/{empId}", response_model = Employee)
def empById(empId: int = Path(None, description = "Enter valid employee id", gt = 0, lt = 3)):
    if(empId in employees):
        return employees[empId]
    else:
        raise Exception("Employee not exist with given id " + str(empId))