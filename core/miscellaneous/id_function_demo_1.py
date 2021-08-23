class Employee:  
    def __init__(self, id, name):  
        self.id = id  
        self.name = name  

emp1 = Employee(1,"Ram")
emp2 = Employee(1,"Ram")
emp3 = Employee(1,"Ram")      

print('id(emp1) -> ' + str(id(emp1)))
print('id(emp2) -> ' + str(id(emp2)))
print('id(emp3) -> ' + str(id(emp3)))