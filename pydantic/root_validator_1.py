from pydantic import (
    BaseModel, 
    ValidationError, 
    validator,
    root_validator
)

from typing import Optional

class Box(BaseModel):
    id: int
    weight: int = None
    height: int = None

    @root_validator
    def allValidator(cls, values):
        if(values == None):
            raise ValueError('id, weight and height must set to a value')

        idTemp = values.get('id')
        weightTemp = values.get('weight')
        heightTemp = values.get('height')

        err = '';
        if(idTemp < 1):
            err = err + 'id must > 0. '

        if(weightTemp < 10):
            err = err + 'weigh must >= 10. '

        if(heightTemp < 15):
            err = err + 'height must >= 15'

        if(len(err) > 1):
            raise ValueError(err)

        return values

try:
    b1 = Box(id = -1, weight = 0, height=16)
    print(b1)
except ValidationError as e:
    print(e.json())
