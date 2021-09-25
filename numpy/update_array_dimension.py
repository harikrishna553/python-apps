import numpy as np

numpy_array = np.arange(20)

print('numpy_array -> ', numpy_array)
print('numpy_array.shape -> ', numpy_array.shape)

print('\nset the dimension to (4,5)')

numpy_array.shape = (4, 5)

print('\nnumpy_array -> ', numpy_array)
print('numpy_array.shape -> ', numpy_array.shape)