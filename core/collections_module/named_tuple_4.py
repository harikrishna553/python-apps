from collections import namedtuple

Employee = namedtuple("Employee", "id age name")
emp1 = Employee(1, 32, 'Krishna')
print(emp1)

Employee = namedtuple("Employee", "id,age,name")
emp1 = Employee(1, 32, 'Krishna')
print(emp1)

Employee = namedtuple("Employee", ['id', 'age', 'name'])
emp1 = Employee(1, 32, 'Krishna')
print(emp1)
