from enum import Enum

class Test(Enum):        
    A = 1
    B = 1
    C = 23

for member in Test:
    print(member, ' -> ', member.value)