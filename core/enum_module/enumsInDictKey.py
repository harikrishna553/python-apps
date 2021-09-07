from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

quotes = {}
quotes[Day.MONDAY] = 'Journey started'
quotes[Day.SATURDAY] = 'Happy week end'

print(quotes)