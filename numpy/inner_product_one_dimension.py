import numpy as np

temp_list1 = [2, 3, 5]
temp_list2 = [1, 2, 4]

arr1 = np.array(temp_list1)
arr2 = np.array(temp_list2)

inner_prodct = np.inner(arr1, arr2)

print('arr1 -> ', arr1)
print('arr2 -> ', arr2)
print('inner_prodct -> ', inner_prodct)