import numpy as np

list1 = [
    [1, 2, 3],
    [4, 5, 6]
]

list2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

matrix1 = np.array(list1, np.int32)
matrix2 = np.array(list2, np.int32)

matrix_mul_result = np.matmul(matrix1, matrix2)
dot_product_result = np.dot(matrix1, matrix2)

print('matrix1 :\n', matrix1)
print('\nmatrix2 :\n ', matrix2)
print('\nmatrix_mul_result :\n ', matrix_mul_result)
print('\ndot_product_result :\n ', dot_product_result)