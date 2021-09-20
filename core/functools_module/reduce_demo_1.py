import functools

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = functools.reduce(lambda x, y : x + y, numbers, 0)
product_of_numbers = functools.reduce(lambda x, y : x * y, numbers, 1)

print('numbers -> ', numbers)
print('sum_of_numbers -> ', sum_of_numbers)
print('product_of_numbers -> ', product_of_numbers)