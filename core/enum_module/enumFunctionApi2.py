from enum import Enum

Color = Enum('Color', [("RED", 20), ("GREEN", 21), ("BLUE", 45)])

print(list(Color))
print(Color['RED'].name, ' -> ', Color['RED'].value)
print(Color['GREEN'].name, ' -> ', Color['GREEN'].value)
print(Color['BLUE'].name, ' -> ', Color['BLUE'].value)