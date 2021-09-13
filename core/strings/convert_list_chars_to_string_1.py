def convert_list_to_string(my_list):
    str = ''

    for ch in my_list:
        str += ch
    
    return str

my_list = ['H', 'e', 'l', 'l', 'o']
my_str = convert_list_to_string(my_list)

print('my_list -> ', my_list)
print('my_str -> ', my_str)