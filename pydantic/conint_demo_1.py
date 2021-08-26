from pydantic import (
    BaseModel,
    conint,
    ValidationError
)

class Employee(BaseModel):
    id: int
    name: str
    age: conint(gt = 18)

try:
    emp1 = Employee(id = 1, name = 'Krishna', age = 17)
except ValidationError as e:
    print(e.json())
