emps = {
    1 : {
        "name" : "Krishna",
        "age": 32
    },
    2 : {
        "name" : "Ram",
        "age": 33
    }
}

def is_key_exist_check_1(dict, key):
    if(key in dict):
        print("{} -> {}".format(key, dict[key]))
    else:
        print("key {} not present".format(key))

def is_key_exist_check_2(dict, key):
    if(dict.has_key(key)):
        print("{} -> {}".format(key, dict[key]))
    else:
        print("key {} not present".format(key))

is_key_exist_check_1(emps, 2)
is_key_exist_check_1(emps, 20)
is_key_exist_check_2(emps, 2)
is_key_exist_check_2(emps, 20)