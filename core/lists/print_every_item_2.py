def print_every_item(my_list):
    no_of_items = len(my_list)
    count = 0

    while count < no_of_items:
        print(my_list[count])
        count += 1
    
print_every_item([2, 3, 5, 7])