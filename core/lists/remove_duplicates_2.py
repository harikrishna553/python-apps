def remove_duplicates(my_list):
    return list(set(my_list))

my_list = [2, 3, 4, 5, 3, 4]
new_list = remove_duplicates(my_list)

print("my_list -> ", my_list)
print("new_list -> ", new_list)