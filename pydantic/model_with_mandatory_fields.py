from pydantic import BaseModel, Field, ValidationError

class Employee(BaseModel):
    id: int
    name: str = ...
    age: int = Field(...)

try:
    emp1 = Employee(name = 'Krishna', age = 23)
except ValidationError as e:
    print(e.json() + '\n\n')

try:
    emp1 = Employee(id=1, age = 23)
except ValidationError as e:
    print(e.json() + '\n\n')

try:
    emp1 = Employee(id = 1, name = 'Krishna')
except ValidationError as e:
    print(e.json() + '\n\n')