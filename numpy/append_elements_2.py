import numpy as np

empty_array = np.empty((0, 4), int)
arr1 = np.append(empty_array, np.array([[2, 3, 5, 7]]), axis=0)
arr1 = np.append(arr1, np.array([[11, 13, 17, 19]]), axis=0)

print('arr1 ->\n', arr1)
