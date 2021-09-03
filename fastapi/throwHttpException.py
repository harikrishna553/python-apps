from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

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
    
@app.get("/emps/by-id/{empId}")
def empById(empId: int = Path(None, description = "Enter valid employee id")):
    if(empId not in emps):
        raise HTTPException(status_code=404, detail="Employee not found")
    return emps[empId]    
