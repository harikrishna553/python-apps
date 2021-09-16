def odd_number_gen(max_number):
    count = 1

    while count < max_number:
        yield count

        count += 2

try:
    state = odd_number_gen(10)
    while True:
        print(next(state))
except StopIteration:
    pass