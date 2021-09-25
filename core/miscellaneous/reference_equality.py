class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

emp1 = Employee(1, 'Krishna')
emp2 = Employee(1, 'Krishna')
emp3 = emp1

print('emp1 is emp2 : ', (emp1 is emp2))
print('emp1 is emp3 : ', (emp1 is emp3))
print('emp2 is emp3 : ', (emp2 is emp3))

print('id(emp1) == id(emp2) : ', (id(emp1) == id(emp2)))
print('id(emp1) == id(emp3) : ', (id(emp1) == id(emp3)))
print('id(emp2) == id(emp3) : ', (id(emp2) == id(emp3)))
