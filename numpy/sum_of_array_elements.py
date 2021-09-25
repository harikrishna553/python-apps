import numpy as np

arr1 = np.array([2, 3, 5])

arr2 = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

sum1 = np.sum(arr1)
sum2 = np.sum(arr2)

print('arr1 : \n', arr1)
print('\narr2 : \n', arr2)

print('\nsum of elements of arr1 : ', sum1)
print('\nsum of elements of arr2: ', sum2)