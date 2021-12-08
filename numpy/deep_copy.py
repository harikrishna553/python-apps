import numpy as np

arr1 = np.arange(10)
arr1_copy = arr1.copy().reshape(2, 5)

print('arr1 -> ', arr1)
print('arr1_copy -> \n', arr1_copy)

print('\nUpdating the values using arr1_copy\n')

arr1_copy[0][1] = 111
arr1_copy[1][2] = 1111

print('arr1 -> ', arr1)
print('arr1_copy -> \n', arr1_copy)