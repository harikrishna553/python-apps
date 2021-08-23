from pydantic import BaseModel, ValidationError
from typing import List

class Address(BaseModel):
    street: str
    city: str
    country: str

class Employee(BaseModel):
    id: int
    name: str
    age: int
    addresses: List[Address]

emp1 = Employee(id = 1, name = 'Ptr', age = 23, addresses = 
    [
    Address(street = 'Chowdeswari', city = "Bangalore", country = 'India'),
    Address(street = 'Panchayat street', city = "Amaravathi", country = 'India'),
    ]
)

emp1Json = emp1.json(exclude={'addresses': {'__all__': {'city'}}})
print(emp1Json)