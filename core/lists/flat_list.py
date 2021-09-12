def flat_list(tempList):
    if(len(tempList) == 0):
        return tempList
    if isinstance(tempList[0], list):
        return flat_list(tempList[0]) + flat_list(tempList[1:])
    return tempList[:1] + flat_list(tempList[1:])
    
list_of_lists = [[2, 3, 5, 7, 11], [1, 3, 5], [2, 4, 6], [[1, 2, [3, 4, 5]]]]
result_list = flat_list(list_of_lists)

print(result_list)