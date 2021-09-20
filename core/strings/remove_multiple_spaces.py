def remove_multiple_spaces(input_str):
    splits = input_str.split()
    return ' '.join(splits)

input_str = '  Hello    World   How  are  you  '
result_str = remove_multiple_spaces(input_str)

print('input_str "', input_str, '"')
print('result_str "', result_str, '"')