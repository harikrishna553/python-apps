numbers = [1, 2, 3, 4, 5]

twice_numbers = map(lambda x : 2 *x, numbers)
square_numbers = map(lambda x : x ** 2, numbers)
cube_numbers = map(lambda x : x ** 3, numbers)

print('numbers -> ', numbers)
print('twice_numbers -> ', list(twice_numbers))
print('square_numbers -> ', list(square_numbers))
print('cube_numbers -> ', list(cube_numbers))
