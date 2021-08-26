from pydantic import (
    BaseModel,
    constr,
    ValidationError
)

class Box(BaseModel):
    id: int
    address: constr(to_lower=True)

try:
    box1 = Box(id = 1, address='BANAGALORE, Chodeswari street')
    print(box1.json())
except ValidationError as e:
    print(e.json())
