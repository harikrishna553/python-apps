from pydantic import BaseModel
from pathlib import Path

class Employee(BaseModel):
    id: int
    name: str
    age: int

path = Path('parseFile.json')
path.write_text('{"id": 1, "name": "Krishna", "age": 32}')
emp1 = Employee.parse_file(path)
emp1Json = emp1.json()
print(emp1Json)