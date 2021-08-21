from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    id: int
    name: str
    age: int

print('\nInitializing with incompatible id\n')
try:
    emp1 = Employee(id = 'aa', name = 'Krishna', age = 23)
    print(emp1)

except ValidationError as e:
    print(e)

print('\nInitializing with compatible values\n')
try:
    emp1 = Employee(id = 1, name = 'Krishna', age = 23)
    print(emp1)
except ValidationError as e:
    print(e)