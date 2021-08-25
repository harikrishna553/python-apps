from typing import TypeVar, Generic
from pydantic.generics import GenericModel

TypeX = TypeVar('TypeX')
TypeY = TypeVar('TypeY')

class Point(GenericModel, Generic[TypeX, TypeY]):
    x: TypeX
    y: TypeY

point1 = Point[int, int](x=1, y=2)
point2 = Point[str, str](x='1', y='2')
print(point1)
print(point2)