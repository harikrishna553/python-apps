class ParentClazz:
    def welcome(self):
        return "Hi!!!!!"

class ChildClazz(ParentClazz):
    def welcome(self):
        return "Good Morning!!!"

obj = ChildClazz()
print(obj.welcome())