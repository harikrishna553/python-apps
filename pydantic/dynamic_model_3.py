from pydantic import BaseModel, create_model, validator, ValidationError

def name_alphanumeric(cls, v):
    assert v.isalnum(), 'must be alphanumeric'
    return v

def age_is_greater_18(cls, v):
    assert v > 18, 'Age must be > 18'
    return v

validators = {
    'username_validator': validator('name')(name_alphanumeric),
    'userage_validator': validator('age')(age_is_greater_18)
}

EmployeeModel = create_model(
    'EmployeeModel', 
    id=(int,...), 
    name=(str,...),
    org = 'ABC Corporation',
    age=(int,...),
    __validators__=validators
    )

try:
    emp1 = EmployeeModel(id=1, name='Krishna!@', street='Chowdeswari', city='Bangalore', age=15)
except ValidationError as e:
    print(e.json())