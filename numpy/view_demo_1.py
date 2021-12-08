import numpy as np

arr1 = np.arange(10)
arr1_view = arr1.view().reshape(2, 5)

print('arr1 -> ', arr1)
print('arr1_view -> \n', arr1_view)

print('\nUpdating the values using view\n')

arr1_view[0][1] = 111
arr1_view[1][2] = 1111

print('arr1 -> ', arr1)
print('arr1_view -> \n', arr1_view)