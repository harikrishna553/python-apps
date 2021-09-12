def first_n_elements(my_list, n):
    temp_list = []

    for i in range(n):
        temp_list.append(my_list[i])
    
    return temp_list

list1 = [2, 3, 4, 5, 7, 11, 13, 17]
first_4_elements = first_n_elements(list1, 4)

print("list1 -> ", list1)
print("first_4_elements -> ", first_4_elements)