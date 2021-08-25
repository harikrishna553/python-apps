from collections import namedtuple

Employee = namedtuple("Employee", "id age name")
emp1 = Employee(id = 1, age = 32, name = 'Krishna')
print(emp1._asdict())