from collections import namedtuple
from pydantic import BaseModel, create_model_from_namedtuple

Point = namedtuple('Point', 'x y')

PointM = create_model_from_namedtuple(Point)

point1 = PointM(x = 1, y = 2)
print(point1)