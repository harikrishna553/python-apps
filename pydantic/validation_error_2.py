from pydantic import BaseModel, ValidationError, conint, constr

class Employee(BaseModel):
    id: int
    name: constr(min_length=3, max_length=10)
    age: conint(gt=18)

try:
    emp1 = Employee(id = 1, name = 'Pt', age = 8)
except ValidationError as e:
    print(e.errors())
    print('\n\n\n')
    print(e.json())
    print('\n\n\n')
    print(str(e))