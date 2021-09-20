class Arithmetic:
    
    def arith(self, a, b):
        self.sum = a + b
        self.sub = a - b
        self.mul = a * b
        self.div = a / b

        return self

obj = Arithmetic()
obj.arith(10, 2)

print('sum of 10 and 2 is ', obj.sum)
print('subtract of 10 and 2 is ', obj.sub)
print('multiplication of 10 and 2 is ', obj.mul)
print('Division of 10 and 2 is ', obj.div)