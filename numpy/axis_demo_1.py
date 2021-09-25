import numpy as np

array = np.array([
    [2, 3, 5, 7], 
    [1, 4, 5, 6]])

sum_by_column_wise = np.sum(array, axis=0)

print(sum_by_column_wise)