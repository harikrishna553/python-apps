from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    age: int

    @validator('name')
    def nameValidator(cls, value):
        if(len(value)< 5):
            raise ValueError('name must contain atleast 5 characters')
        return value
    
    @validator('age')
    def ageValidator(cls, value):
        if(value < 18):
            raise ValueError('age should be >= 18')
        return value

try:
    emp1 = Employee(id = 1, age = 17, name='kri')
    print(emp1)
except ValidationError as e:
    print(e.json())