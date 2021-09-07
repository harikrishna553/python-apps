from enum import Enum

class Test(Enum):        
    A = 1
    B = 1
    C = 23

print('list(Test) -> ', list(Test))
print('Test.__members__ -> ' ,Test.__members__)

print('\nIterating over Test.__members__')
for member in Test.__members__.items():
    # member represent a tuple
    print(member[0], '->', member[1])