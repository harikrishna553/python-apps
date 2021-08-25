from collections import namedtuple

Employee = namedtuple("Employee", "id age name")

print('issubclass(Employee, tuple) -> ' + str(issubclass(Employee, tuple)))