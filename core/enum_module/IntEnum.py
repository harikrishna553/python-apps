from enum import IntEnum

class PrimeNumbers(IntEnum):
    TWO = 2
    THREE = 3
    FIVE = 5
    SEVEN = 7

class EvenNumbers(IntEnum):
    TWO = 2
    FOUR = 4
    SIX = 6
    EIGHT = 8

class OddNumbers(IntEnum):
    ONE = 1
    THREE = 3
    FIVE = 5
    SEVEN = 7


print('PrimeNumbers.TWO == 2', ' -> ', PrimeNumbers.TWO == 2)
print('PrimeNumbers.TWO == EvenNumbers.TWO', ' -> ', PrimeNumbers.TWO == EvenNumbers.TWO)
print('PrimeNumbers.TWO == OddNumbers.ONE', ' -> ', PrimeNumbers.TWO == OddNumbers.ONE)
