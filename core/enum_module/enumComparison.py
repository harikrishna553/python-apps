from enum import Enum

class Test(Enum):        
    A = 1
    B = 1
    C = 23

print('Test.A == Test.A : ', (Test.A == Test.A))
print('Test.A is Test.A : ', (Test.A is Test.A))

# Aliases always return True
print('Test.A == Test.B : ', (Test.A == Test.B))
print('Test.A is Test.B : ', (Test.A is Test.B))

print('Test.A == Test.C : ', (Test.A == Test.C))
print('Test.A is Test.C : ', (Test.A is Test.C))