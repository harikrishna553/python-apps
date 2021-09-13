def count_lowercase_characters(input_str):
    count = 0

    for ch in input_str:
        if ch.islower():
            count += 1

    return count

input = 'Hello WorlD'

print('Number of lowercase characters in "',input,'" is ', count_lowercase_characters(input))