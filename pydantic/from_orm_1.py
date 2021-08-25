from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()

class EmployeeOrm(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), unique=True)
    age = Column(Integer, nullable=False)


class EmployeeModel(BaseModel):
    id: int
    name: constr(max_length=63)
    age: int

    class Config:
        orm_mode = True


empOrm = EmployeeOrm(
    id=123,
    name='Krishna',
    age=31
)
print('empOrm -> ' + str(empOrm))
empModel = EmployeeModel.from_orm(empOrm)
print('empModel -> ' + str(empModel))