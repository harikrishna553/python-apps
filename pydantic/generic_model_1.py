from typing import TypeVar, Generic
from pydantic.generics import GenericModel

TypeX = TypeVar('TypeX')

class Point(GenericModel, Generic[TypeX]):
    x: TypeX

point1 = Point[int](x=1)
point2 = Point[str](x='1')
print(point1)
print(point2)