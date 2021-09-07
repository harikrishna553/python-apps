from enum import Enum

class Color(Enum):
    RED = 121
    GREEN = 255
    BLUE = 30

print(Color['RED'])
print(Color['GREEN'])
print(Color['BLUE'])