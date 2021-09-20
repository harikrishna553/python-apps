def unique_elements(my_list):
    return list(set(my_list))
    
numbers = [1, 2, 3, 4, 2, 3, 4, 5]
unique_numbers = unique_elements(numbers)

print('numbers -> ', numbers)
print('unique_numbers -> ', unique_numbers)
