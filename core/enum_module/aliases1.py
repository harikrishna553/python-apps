from enum import Enum

class Test(Enum):        
    A = 1
    B = 1
    C = 23

print(Test(1))
print(Test(23))