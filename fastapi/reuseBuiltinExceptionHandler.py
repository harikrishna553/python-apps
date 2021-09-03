from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from fastapi.exception_handlers import (
    http_exception_handler
)

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

@app.exception_handler(HTTPException)
async def emp_not_found_exception_handler(request: Request, exc: HTTPException):
    print(f"Oops!!! received HTTPException : {exc}")
    return await http_exception_handler(request, exc)

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
        raise HTTPException(
                status_code=404, 
                detail={"msg" : "Employee not found", "id" : empId}
            )
            
    return emps[empId]    
