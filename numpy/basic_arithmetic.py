import numpy as np

test_list = [2, 3, 5, 7, 11]

numpy_array = np.array(test_list)

print('test_list -> ', test_list)
print('numpy_array -> ', numpy_array)

add_by_5 = (numpy_array + 5)
print('add_by_5 -> ', add_by_5)

subtract_by_5 = (numpy_array - 5)
print('subtract_by_5 -> ', subtract_by_5)

multiply_by_5 = (numpy_array * 5)
print('multiply_by_5 -> ', multiply_by_5)

divide_by_5 = (numpy_array / 5)
print('divide_by_5 -> ', divide_by_5)