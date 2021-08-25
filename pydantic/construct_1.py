from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee(id = 1, name = 'Krishna', age = 23)
emp1Dict = emp1.dict();

emp1Construct = Employee.construct(**emp1Dict)

print('emp1 -> ' + str(emp1))
print('emp1Dict -> ' + str(emp1Dict))
print('emp1Construct -> ' + str(emp1Construct))