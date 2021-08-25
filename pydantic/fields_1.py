from pydantic import BaseModel

class Employee(BaseModel):
    id: int = None
    name: str = None
    age: int = None
    
emp1 = Employee()
emp2 = Employee(id = 1)
emp3 = Employee(id = 1, name = 'Krishna')
emp4 = Employee(id = 1, name = 'Krishna', age = 23)

print(emp1.__fields__)
print('\n')
print(emp2.__fields__)
print('\n')
print(emp3.__fields__)
print('\n')
print(emp4.__fields__)
print('\n')