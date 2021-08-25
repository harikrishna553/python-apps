from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        allow_mutation = False

emp1 = Employee(id = 1, name = 'Krishna', age = 23)

print('updating employee name')
emp1.name = 'Ram'