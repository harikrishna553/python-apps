def get_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        print('Input is not a valid integer')

res1 = get_int('1234')
print('res1 -> ', res1, '\n')

res2 = get_int('56aa78')
print('res2 -> ', res2)

