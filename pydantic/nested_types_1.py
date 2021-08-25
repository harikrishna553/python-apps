from pydantic import BaseModel, ValidationError

class Address(BaseModel):
    street: str
    city: str
    country: str

class Employee(BaseModel):
    id: int
    name: str
    age: int
    address: Address

emp1 = Employee(id = 1, name = 'Ptr', age = 23, address = Address(street = 'Chowdeswari', city = "Bangalore", country = 'India'))

emp1Json = emp1.json(exclude = {'address' : {'street', 'country'}})
emp2Json = emp1.json(exclude = {'address' : {'street', 'country'}, 'age': ...})

print('emp1Json -> ' + emp1Json)
print('emp2Json -> ' + emp2Json)
