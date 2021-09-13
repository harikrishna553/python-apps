def count_digits(input_str):
    count = 0

    for ch in input_str:
        if ch.isdigit():
            count += 1

    return count

input = '123Hello Wo12rlD'

print('Number of digits in "',input,'" is ', count_digits(input))