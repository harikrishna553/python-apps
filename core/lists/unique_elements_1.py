def unique_elements(my_list):
    unique_list = []

    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

numbers = [1, 2, 3, 4, 2, 3, 4, 5]
unique_numbers = unique_elements(numbers)

print('numbers -> ', numbers)
print('unique_numbers -> ', unique_numbers)
