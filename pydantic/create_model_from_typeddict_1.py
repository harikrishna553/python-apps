from typing_extensions import TypedDict

from pydantic import ValidationError, create_model_from_typeddict

class Employee(TypedDict):
    name: str
    id: int

EmployeeM = create_model_from_typeddict(Employee)

emp1 = EmployeeM(id=1, name='Krishna')
print(emp1.json())