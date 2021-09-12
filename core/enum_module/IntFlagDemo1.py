from enum import IntFlag

class IntBits(IntFlag):
    ONE = 1
    TWO = 2
    FOUR = 4
    EIGHT = 8

two_or_four = IntBits.TWO | IntBits.FOUR
one_or_two_or_four_eight = IntBits.ONE | IntBits.TWO | IntBits.FOUR | IntBits.EIGHT

print(two_or_four, ' -> ', two_or_four.value)
print(one_or_two_or_four_eight, ' -> ', one_or_two_or_four_eight.value)

print("IntBits.TWO == 2", " -> ", IntBits.TWO == 2)