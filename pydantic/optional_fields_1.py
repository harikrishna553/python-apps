from pydantic import BaseModel, ValidationError
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    age: Optional[int]

try:
    emp1 = Employee(id = 1, name = 'Krishna')
    print(emp1)
except ValidationError as e:
    print(e.json() + '\n\n')