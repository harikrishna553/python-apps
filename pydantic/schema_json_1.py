from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp1 = Employee(id = 1, name = 'Krishna', age = 23)
emp1JsonSchema = Employee.schema_json(indent=2)

print('emp1 -> ' + str(emp1) + '\n\n')
print('emp1JsonSchema -> ' + emp1JsonSchema)