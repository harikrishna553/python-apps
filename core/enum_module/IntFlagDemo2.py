from enum import IntFlag

class IntBits(IntFlag):
    ONE = 1
    TWO = 2
    FOUR = 4
    EIGHT = 8

print("IntBits.TWO == 2", " -> ", IntBits.TWO == 2)
print("IntBits.TWO | 4", " -> ", (IntBits.TWO | 4).value)