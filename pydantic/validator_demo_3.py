from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class Person(BaseModel):
    id: int
    name: str
    age: int

    @validator('age', 'id')
    def ageAndIdValidator(cls, value):
        if(value < 1):
            raise ValueError('id and age must > 0')
        return value

try:
    p1 = Person(id = -1, age = -1, name='kri')
    print(p1)
except ValidationError as e:
    print(e.json())
