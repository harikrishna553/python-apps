def last_n_elements(my_list, n):
    size_of_list = len(my_list)
    start_index = size_of_list - n
    return my_list[start_index:size_of_list]

list1 = [2, 3, 4, 5, 7, 11, 13, 17]
first_4_elements = last_n_elements(list1, 4)

print("list1 -> ", list1)
print("last_4_elements -> ", first_4_elements)