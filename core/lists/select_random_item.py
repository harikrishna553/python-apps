import random

def get_rand_item(my_list):
    return random.choice(my_list)

my_list = [2, 3, 5, 7, 11, 13, 17, 19]

print(get_rand_item(my_list))
print(get_rand_item(my_list))
print(get_rand_item(my_list))