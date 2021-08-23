from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee(id = 1, name = 'Krishna', age = 23)
empDict1 = emp1.dict()
empDict2 = emp1.dict(include= {'id', 'name'})
empDict3 = emp1.dict(exclude= {'age'})

print('empDict1 -> ' + str(empDict1))
print('empDict2 -> ' + str(empDict2))
print('empDict3 -> ' + str(empDict3))