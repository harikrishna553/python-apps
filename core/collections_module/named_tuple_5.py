from collections import namedtuple

Employee = namedtuple("Employee", "id _age name")
emp1 = Employee(1, 32, 'Krishna')
print(emp1)