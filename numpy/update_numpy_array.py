import numpy as np

test_list = [2, 3, 5, 7, 11]
numpy_array = np.array(test_list)

print('numpy_array -> ', numpy_array)

print('\nUpdating the value at index 0 to 13 and 2 to 17')

numpy_array[0] = 13
numpy_array[2] = 17

print('\nnumpy_array -> ', numpy_array)