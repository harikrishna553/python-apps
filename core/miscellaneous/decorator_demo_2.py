def logAndAdd(func):
    def log(a, b):
        print('inputs: ', a, b)
        return func(a, b)
    return log

@logAndAdd
def add(a, b):
    return a + b

print('sum of 10 and 20 is ', add(10, 20))
