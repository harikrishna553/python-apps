import numpy as np

numpy_array = np.arange(20)
numpy_array.shape = (4, 5)

print('numpy_array\n', numpy_array)
print('element at 2nd row and 3rd column : ', numpy_array[1][2])

print('update the element at 3rd row and 2nd column to 10000')
numpy_array[2][1] = 10000

print('\nnumpy_array\n', numpy_array)