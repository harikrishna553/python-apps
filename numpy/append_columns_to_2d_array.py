import numpy as np

arr1 = np.array([[2, 11], [3, 13], [5, 17], [7, 19]])

print('arr1 -> \n', arr1)

arr1 = np.append(arr1, np.array([[23, 29, 31, 37]]).transpose(), axis=1)

print('\narr1 ->\n', arr1)
