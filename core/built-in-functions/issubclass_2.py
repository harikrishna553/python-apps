from collections import namedtuple

Employee = namedtuple("Employee", "id age name")

print('issubclass(Employee, (tuple, Employee)) -> ' + str(issubclass(Employee, (tuple, Employee))))
print('issubclass(Employee, (tuple, Employee, list)) -> ' + str(issubclass(Employee, (tuple, Employee, list))))