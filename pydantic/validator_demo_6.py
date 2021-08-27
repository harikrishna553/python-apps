from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class Box(BaseModel):
    id: int
    weight: int = None
    height: int = None

    @validator('*', always=True)
    def allValidator(cls, value):
        if(value == None):
            raise ValueError('id, weight and height must set to a value')
        if(value < 1):
            raise ValueError('id, weight and height must > 0')
        return value

try:
    b1 = Box(id = 1, weight = 0)
    print(b1)
except ValidationError as e:
    print(e.json())
