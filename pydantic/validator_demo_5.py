from pydantic import BaseModel, ValidationError, validator
from typing import List

class Test(BaseModel):
    even_numbers: List[int]

    @validator('even_numbers', each_item=True)
    def evenNumValidator(cls, value):
        if(value % 2 != 0):
            raise ValueError('number must be even')
        return value

try:
    t1 = Test(even_numbers = [2, 4, 6])
    print(t1)

    t2 = Test(even_numbers = [2, 4, 5, 6, 7])
    print(t2)
except ValidationError as e:
    print(e.json())
