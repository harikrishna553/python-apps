from collections import namedtuple

Employee = namedtuple("Employee", "id age name")

emp1 = Employee(1, 32, 'Krishna')

print(emp1)
print('\n')

print('id -> ' + str(emp1.id))
print('age -> ' + str(emp1.age))
print('name -> ' + str(emp1.name))

print('\n')
print('id -> ' + str(emp1[0]))
print('age -> ' + str(emp1[1]))
print('name -> ' + str(emp1[2]))