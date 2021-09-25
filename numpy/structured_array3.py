import numpy as np

arr1 = np.zeros(4, dtype={
    'names':('id', 'name', 'age', 'height', 'weight'),
    'formats':('i8', 'U10', 'i8', 'f8', 'f8')
    })

ids = [1, 2, 3, 4]
names = ['Ram', 'Rahim', 'Robert', 'Sailu']
ages = [41, 52, 23, 32]
heights = [5.7, 5.9, 6.1, 5.4]
weights = [81.7, 74, 85, 71]

arr1['id'] = ids
arr1['name'] = names
arr1['age'] = ages
arr1['height'] = heights
arr1['weight'] = weights

print('arr1 : \n', arr1)
