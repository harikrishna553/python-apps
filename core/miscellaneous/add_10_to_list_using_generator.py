my_list = [2, 3, 4, 7]

def inc_by_10(x):
    return x + 10

inc_by_10_generator = (inc_by_10(x) for x in my_list)

print(next(inc_by_10_generator))
print(next(inc_by_10_generator))
