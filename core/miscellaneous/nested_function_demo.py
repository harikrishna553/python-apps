def arithmetic(a, b):
    def sum(a, b):
        return a + b
    
    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    print('Sum of ', a, ' and ', b, ' is : ', sum(a, b))
    print('Subtraction of ', a, ' and ', b, ' is : ', sub(a, b))
    print('Multiplication of ', a, ' and ', b, ' is : ', mul(a, b))
    print('Division of ', a, ' and ', b, ' is : ', div(a, b))

arithmetic(10, 20)