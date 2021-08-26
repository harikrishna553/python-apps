from pydantic import (
    BaseModel,
    conbytes,
    ValidationError
)

class Box(BaseModel):
    id: int
    address: conbytes(to_lower=True, strip_whitespace = True)

try:
    box1 = Box(id = 1, address='    BANAGALORE, Chodeswari street   ')
    print(box1.json())
except ValidationError as e:
    print(e.json())
