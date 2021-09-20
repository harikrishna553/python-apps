def arith(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b

    return [sum, sub, mul, div]

res1, res2, res3, res4 = arith(10, 2)

print('sum of 10 and 2 is ', res1)
print('subtract of 10 and 2 is ', res2)
print('multiplication of 10 and 2 is ', res3)
print('Division of 10 and 2 is ', res4)
