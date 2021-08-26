from pydantic import (
    BaseModel,
    confloat,
    ValidationError
)

class Box(BaseModel):
    id: int
    weight: confloat(lt = 30, gt = 1)

try:
    box1 = Box(id = 1, weight = 50)
except ValidationError as e:
    print(e.json())
