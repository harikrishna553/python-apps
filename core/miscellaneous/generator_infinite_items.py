def fibonacci():
    first = 0
    next = 1

    while True:
        yield first
        temp = next
        next = first + next
        first = temp

# printing first 10 fibonaaci series
i = 0
state = fibonacci()
while i < 10:
    print(next(state))
    i += 1
