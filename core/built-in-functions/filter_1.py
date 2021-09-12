numbers = range(1, 10)

def is_even(number):
    return (number % 2 ) == 0

def is_odd(number):
    return (number % 2) != 0

evenNumbers = list(filter(is_even, numbers))
oddNumbers = list(filter(is_odd, numbers))

print('numbers -> ', list(numbers))
print('evenNumbers -> ', evenNumbers)
print('oddNumbers -> ', oddNumbers)