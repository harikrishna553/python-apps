import numpy as np

emp1 = (1, 'Ram', 41, 5.7, 81.7)
emp2 = (2, 'Rahim', 52, 5.9, 74)
emp3 = (3, 'Robert', 23, 6.1, 85)
emp4 = (4, 'Sailu', 32, 5.4, 71)

arr1 = np.rec.array(obj = [emp1, emp2, emp3, emp4], dtype={
    'names':('id', 'name', 'age', 'height', 'weight'),
    'formats':('i8', 'U10', 'i8', 'f8', 'f8')
    })

print('arr1 : \n', arr1)
print('\nages -> ', arr1['age'])
print('\nname of second employee -> ', arr1[1].name)
print('\nname of second employee -> ', arr1[arr1.age > 45].name)
