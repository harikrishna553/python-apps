from enum import Enum

class Test(Enum):
    def describe(self):
        return self.name, self.value
        
class Test1(Test):        
    A = 1
    B = 1
    C = 23

print(Test1.A.describe())