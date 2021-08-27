from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class Box(BaseModel):
    id: int
    weight: str
    height: int

    @validator('*')
    def ageAndIdValidator(cls, value):
        if(value < 1):
            raise ValueError('id, weight and height must > 0')
        return value

try:
    b1 = Box(id = 1, weight = 0, height = 0)
    print(b1)
except ValidationError as e:
    print(e.json())
