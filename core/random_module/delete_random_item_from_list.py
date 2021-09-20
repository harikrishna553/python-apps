import random

def delete_random_element(my_list):
    element_to_delete = random.choice(my_list)
    my_list.remove(element_to_delete)
    return element_to_delete

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

print('deleted element : ', delete_random_element(primes))
print('primes : ', primes)

print('\ndeleted element : ', delete_random_element(primes))
print('primes : ', primes)

print('\ndeleted element : ', delete_random_element(primes))
print('primes : ', primes)
