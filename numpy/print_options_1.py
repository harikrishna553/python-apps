import numpy as np

arr1 = np.random.standard_normal(size = (3, 4))

print('arr1 : \n', arr1)

print('\nSetting precision to 4 using printoptions\n')
np.set_printoptions(precision=4)

print('arr1 : \n', arr1)
