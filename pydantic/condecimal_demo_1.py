from pydantic import (
    BaseModel,
    condecimal,
    ValidationError
)

class Box(BaseModel):
    id: int
    weight: condecimal(lt = 30, gt = 1, max_digits=4)

try:
    box1 = Box(id = 1, weight = 10.456)
except ValidationError as e:
    print(e.json())
