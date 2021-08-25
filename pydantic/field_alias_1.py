from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int = Field(alias='emp_id')
    name: str = Field(alias='emp_name')
    age: int

emp1 = Employee(emp_id = 1, emp_name = 'Ptr', age = 23)

emp1Json = emp1.json()
emp1JsonByAlias = emp1.json(by_alias=True)

print('emp1Json -> ' + emp1Json)
print('emp1JsonByAlias -> ' + emp1JsonByAlias)
