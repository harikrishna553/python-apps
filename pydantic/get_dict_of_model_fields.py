from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee(id = 1, name = 'Krishna', age = 23)
empDict = emp1.dict()

print('empDict ' + str(empDict))
print('dict(emp1) ' + str(dict(emp1)))