import numpy as np

arr1 = np.array([[2, 3, 5, 7]])
arr1 = np.append(arr1, np.array([[11, 13, 17, 19]]), axis=0)
arr1 = np.append(arr1, np.array([[23, 29, 31, 37]]), axis=0)

print('arr1 ->\n', arr1)
