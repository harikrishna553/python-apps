from fastapi import FastAPI, Path, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class EmployeeNotFoundException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail

@app.exception_handler(EmployeeNotFoundException)
def emp_not_found_exception_handler(request: Request, exc: EmployeeNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail
    )

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
        raise EmployeeNotFoundException(
                status_code=404, 
                detail={"msg" : "Employee not found", "id" : empId}
            )
            
    return emps[empId]    
