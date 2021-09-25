import numpy as np

a = np.arange(6).reshape((3, 2))
b = np.arange(8).reshape((4, 2))

inner_prodct = np.inner(a, b)

print('arr1 -> \n', a)
print('\narr2 -> \n', b)
print('\ninner_prodct -> \n', inner_prodct)