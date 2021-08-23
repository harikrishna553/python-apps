from pydantic import BaseModel, ValidationError

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee(id = 1, name = 'Krishna', age = 23)

emp1Copy1 = emp1.copy()
emp1Copy2 = emp1.copy(include = {'id', 'name'})
emp1Copy3 = emp1.copy(exclude = {'age'})
emp1Copy4 = emp1.copy(exclude = {'name'}, update = {'age' : 45})

print('emp1Copy1 -> ' + str(emp1Copy1))
print('emp1Copy2 -> ' + str(emp1Copy2))
print('emp1Copy3 -> ' + str(emp1Copy3))
print('emp1Copy4 -> ' + str(emp1Copy4))