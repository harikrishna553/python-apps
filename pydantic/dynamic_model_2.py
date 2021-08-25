from pydantic import BaseModel, create_model

class Address(BaseModel):
    street: str = None
    city: str = None
    country: str = None

EmployeeModel = create_model(
    'EmployeeModel', 
    id=(int,...), 
    name=(str,...),
    org = 'ABC Corporation',
    __base__=Address
    )

emp1 = EmployeeModel(id=1, name='Krishna', street='Chowdeswari', city='Bangalore')

print(EmployeeModel.__fields__.keys())
print('emp1 -> ' + emp1.json())