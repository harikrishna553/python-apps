import datetime

def timestamp(func):
    def log(a, b):
        print('time ', datetime.datetime.now())
        return func(a, b)
    return log

def printHeader(func):
    def log(a, b):
        print('---------------------------')
        print('Calculationg sum of two numbers')
        print('a = ', a)
        print('b = ', b)
        print('---------------------------')
        return func(a, b)
    return log

@printHeader
@timestamp
def add(a, b):
    return a + b

print('sum of 10 and 20 is ', add(10, 20))
