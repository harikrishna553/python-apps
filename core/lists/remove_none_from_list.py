data = [2, None, 3, '', True, False, 0]

def is_not_none(element):
    if element is None :
        return False
    return True

data_without_none = list(filter(is_not_none,data))

print('data -> ', data)
print('data_without_none -> ', data_without_none)