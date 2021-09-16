class Employee:
    def __init__(self, id, name, age, country):
        self.id = id
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return str(self.id)+"," +self.name + "," + str(self.age) + ","+self.country

def print_list(my_list, msg):
    print(msg)
    for item in my_list:
        print(item)
    print()

emp1 = Employee(1, "Krishna", 32, 'India')
emp2 = Employee(21, "PTR", 41, 'Canada')
emp3 = Employee(3, "Sankalp", 38, 'Canada')
emp4 = Employee(30, "Sankalp", 29, 'India')
emp5 = Employee(13, "Ramesh", 41, 'India')
emp6 = Employee(15, "Bala", 41, 'Canada')
emp7 = Employee(25, "Lakshman", 41, 'India')
emp8 = Employee(51, "Krishna", 33, 'Canada')

my_emps = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8]

print_list(my_emps, 'Actual list content')

my_emps.sort(key=lambda emp : (emp.age, emp.country))
print_list(my_emps, 'Sort by age and country')

my_emps = sorted(my_emps, key=lambda emp : (emp.country, emp.name))
print_list(my_emps, 'Sort by country and name')