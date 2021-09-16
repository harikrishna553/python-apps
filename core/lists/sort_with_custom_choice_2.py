class Employee:
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return str(self.id)+"," +self.firstName + ","+self.lastName

def print_list(my_list, msg):
    print(msg)
    for item in my_list:
        print(item)
    print()

emp1 = Employee(1, "Krishna", "Gurram")
emp2 = Employee(21, "PTR", "Nayan")
emp3 = Employee(3, "Sankalp", "Dubey")

my_emps = [emp1, emp2, emp3]

print_list(my_emps, 'Actual list content')

my_emps.sort(key=lambda emp : emp.id)
print_list(my_emps, 'Sort by id')

my_emps = sorted(my_emps, key=lambda emp : emp.firstName)
print_list(my_emps, 'Sort by firstName')