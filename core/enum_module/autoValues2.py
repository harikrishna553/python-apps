from enum import Enum, auto

class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = 30
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = 111
    SUNDAY = auto()

for day in Day:
    print(day, ' -> ', day.value)