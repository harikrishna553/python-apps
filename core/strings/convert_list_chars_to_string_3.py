from operator import concat
from functools import reduce

def convert_list_to_string(my_list):
    return reduce(concat, my_list)

my_list = ['H', 'e', 'l', 'l', 'o']
my_str = convert_list_to_string(my_list)

print('my_list -> ', my_list)
print('my_str -> ', my_str)