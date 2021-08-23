from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee(id = 1, name = 'Krishna', age = 23)

emp1Dict = dict(emp1)

print('emp1 -> ' + str(emp1))
print('emp1Dict -> ' + str(emp1Dict))