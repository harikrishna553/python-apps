import copy

class Marks:
    def __init__(self, maths, physics, chemistry):
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry

    def __str__(self):
        return 'maths : ' + str(self.maths) + ', physics : ' + str(self.physics) + ', chemistry : ' + str(self.chemistry)

class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return 'id : ' + str(self.id) + ', name : ' + self.name + ', marks : [' + str(self.marks) + ']'

marks1 = Marks(75, 91, 87)
student1 = Student(1, 'Krishna', marks1)

student2 = copy.deepcopy(student1)

print('student1 details')
print(student1)

print('\nstudent2 details')
print(student2)

print('\nChange marks, id and name of student2')
student2.marks.maths = 97
student2.marks.physics = 98
student2.marks.chemistry = 99

student2.id = 2
student2.name = 'Lahari'

print('\nstudent1 details')
print(student1)

print('\nstudent2 details')
print(student2)




