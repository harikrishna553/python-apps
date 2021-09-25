import numpy as np

arr1 = np.zeros(4, dtype={
    'names':('id', 'name', 'age', 'height', 'weight'),
    'formats':('i8', 'U10', 'i8', 'f8', 'f8')
    })

emp1 = (1, 'Ram', 41, 5.7, 81.7)
emp2 = (2, 'Rahim', 52, 5.9, 74)
emp3 = (3, 'Robert', 23, 6.1, 85)
emp4 = (4, 'Sailu', 32, 5.4, 71)

arr1[0] = emp1
arr1[1] = emp2
arr1[2] = emp3
arr1[3] = emp4

print('arr1 : \n', arr1)
print('\nfields -> ', arr1.dtype.fields)
print('\nnames -> ', arr1.dtype.names)
print('\nages -> ', arr1['age'])
print('\nname of second employee -> ', arr1[1]['name'])
print('\nname of second employee -> ', arr1[arr1['age'] > 45]['name'])
print('\nheight and weight -> ', arr1[['height', 'weight']])