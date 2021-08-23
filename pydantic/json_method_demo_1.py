from pydantic import BaseModel, ValidationError
from datetime import datetime

class Employee(BaseModel):
    id: int
    name: str
    age: int
    dateOfBirth: datetime

emp1 = Employee(id = 1, name = 'Ptr', age = 23, dateOfBirth = datetime(1988, 6, 6, 12, 13, 14))
emp1Json = emp1.json()

print('emp1Json -> ' + emp1Json)