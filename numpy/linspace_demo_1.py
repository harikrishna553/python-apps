import numpy as np

numpy_array1 = np.linspace(2, 20)
numpy_array2 = np.linspace(2, 20, 5)
numpy_array3 = np.linspace(2, 20, 5, endpoint = False)

print('numpy_array1 -> ', numpy_array1)
print('numpy_array2 -> ', numpy_array2)
print('numpy_array3 -> ', numpy_array3)

print('\nGet array and step size')
numpy_tuple = np.linspace(2, 20, 5, retstep = True)
print('array -> ', numpy_tuple[0])
print('step size -> ', numpy_tuple[1])