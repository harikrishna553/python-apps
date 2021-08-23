from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee.parse_obj({'id' : 1, 'name' : 'Krishna', 'age': 32})
emp1Json = emp1.json()
print(emp1Json)