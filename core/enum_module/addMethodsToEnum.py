from enum import Enum

class Test(Enum):        
    A = 1
    B = 1
    C = 23

    def describe(self):
        return self.name, self.value
    
    def __str__(self):
        return 'I am {0} and has value {1}'.format(self.name, self.value)

    @classmethod
    def decribeEnum(cls):
        return "I am Test enum"

print(Test.decribeEnum())
print(Test.C.describe())
print(str(Test.C))