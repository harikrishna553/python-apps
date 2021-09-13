def remove_duplicates(my_list):
    new_list = []

    for item in my_list:
        if item not in new_list:
            new_list.append(item)

    return new_list


my_list = [2, 3, 4, 5, 3, 4]
new_list = remove_duplicates(my_list)

print("my_list -> ", my_list)
print("new_list -> ", new_list)