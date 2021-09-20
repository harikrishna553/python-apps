numbers = [1, 2, 3, 4, 5]

def calc(x, y):
    return x**2, x**3

square_and_cubes = map(calc, numbers, numbers)

print('numbers -> ', numbers)
print('square_and_cubes -> ', list(square_and_cubes))