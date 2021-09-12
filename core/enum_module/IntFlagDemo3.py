from enum import IntFlag

class IntBits1(IntFlag):
    ONE = 1
    TWO = 2

class IntBits2(IntFlag):
    FOUR = 4
    EIGHT = 8

print("IntBits1.TWO | IntBits2.FOUR", " -> ", (IntBits1.TWO | IntBits2.FOUR))
