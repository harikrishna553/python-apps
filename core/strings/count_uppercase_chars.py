def count_uppercase_characters(input_str):
    count = 0

    for ch in input_str:
        if ch.isupper():
            count += 1

    return count

input = 'Hello WorlD'

print('Number of uppercase characters in "',input,'" is ', count_uppercase_characters(input))