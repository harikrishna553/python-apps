def count_lower_upper_digits(input_str):
    result = {
        'upper': 0,
        'lower': 0,
        'digit': 0
    }

    for ch in input_str:
        if ch.isupper():
            result['upper'] += 1
        elif ch.islower():
            result['lower'] += 1
        elif ch.isdigit():
            result['digit'] += 1

    return result

input = '123Hello Wo12rlD'

print('Number of digits, lower and uppercase characters in "',input,'" are ', count_lower_upper_digits(input))