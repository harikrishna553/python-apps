from collections import namedtuple

Employee = namedtuple("Employee", "id age name")

print('issubclass(Employee, tuple) -> ' + str(issubclass(Employee, tuple)))
print('issubclass(Employee, Employee) -> ' + str(issubclass(Employee, Employee)))
print('issubclass(Employee, list) -> ' + str(issubclass(Employee, list)))