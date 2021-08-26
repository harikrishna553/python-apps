from pydantic import (
    BaseModel,
    conset,
    ValidationError
)

class Employee(BaseModel):
    id: int
    name: str
    age: int
    hobbies: conset(str, min_items=2, max_items=4)

try:
    emp1 = Employee(id = 1, name = 'Krishna', age = 23, hobbies = {'Cooking'})
except ValidationError as e:
    print(e.json())
