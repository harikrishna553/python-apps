class Employee:
    """ Employee class """
    totalEmployees=0  # Class level variable
  
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        Employee.totalEmployees = Employee.totalEmployees + 1
  
    def noOfEmployees(cls):
        return Employee.totalEmployees

Employee.countEmps = classmethod(Employee.noOfEmployees)

emp1 = Employee(1, "Krishna", "Gurram")
print("Total Employees", Employee.countEmps())

emp2 = Employee(1, "Lahari", "Thulasi")
print("Total Employees", Employee.countEmps())