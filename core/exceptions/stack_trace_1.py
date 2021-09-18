import traceback
import sys

def interest_calc(principal, time, rateOfIntrest):
    assert principal > 1
    assert time > 1 and time < 100
    assert rateOfIntrest > 1 and rateOfIntrest < 5

    return (principal * time * rateOfIntrest) / 1000

def demo(principal, time, rateOfIntrest):
    try:
        interest_calc(principal, time, rateOfIntrest)
    except AssertionError:
        traceback.print_exception(*sys.exc_info())

demo(0, 10, 5)
