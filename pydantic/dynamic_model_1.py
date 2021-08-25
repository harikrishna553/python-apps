from pydantic import BaseModel, create_model

EmployeeModel = create_model('EmployeeModel', id=(int,...), name=(str,...))

emp1 = EmployeeModel(id=1, name='Krishna')

print(EmployeeModel.__fields__.keys())
print('emp1 -> ' + emp1.json())