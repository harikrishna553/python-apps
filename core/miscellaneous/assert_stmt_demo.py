import traceback

def interest_calc(principal, time, rateOfIntrest):
    assert principal > 1
    assert time > 1 and time < 100
    assert rateOfIntrest > 1 and rateOfIntrest < 5

    return (principal * time * rateOfIntrest) / 1000

def demo(principal, time, rateOfIntrest):
    try:
        interest_calc(principal, time, rateOfIntrest)
    except AssertionError:
        traceback.print_exc()

demo(0, 10, 5)

print('\n\n')
demo(10, 1000, 5)