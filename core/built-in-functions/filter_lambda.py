numbers = range(1, 10)

evenNumbers = list(filter(lambda x: (x%2 == 0), numbers))
oddNumbers = list(filter(lambda x: (x%2 != 0), numbers))

print('numbers -> ', list(numbers))
print('evenNumbers -> ', evenNumbers)
print('oddNumbers -> ', oddNumbers)