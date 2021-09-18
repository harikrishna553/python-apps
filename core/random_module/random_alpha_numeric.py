import random

def generate_random_string(length_of_str):
    input = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    size_of_input = len(input)

    for i in range(length_of_str):
        random_index = random.randint(0, size_of_input-1)
        result += input[random_index]

    return result


print(generate_random_string(5))
print(generate_random_string(6))
print(generate_random_string(7))
print(generate_random_string(8))
