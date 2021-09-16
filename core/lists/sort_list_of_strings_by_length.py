def print_list(my_list, msg):
    print(msg)
    for item in my_list:
        print(item)
    print()

countries1 = ['Albania', 'Canada', 'Australia', 'India', 'Chile', 'Bhutan']
countries2 = ['Albania', 'Canada', 'Australia', 'India', 'Chile', 'Bhutan']

countries1.sort(key=len)

countryies2_by_length = sorted(countries2, key=len)

print_list(countries1, "Sorted by length using sort method")
print_list(countryies2_by_length, "Sorted by length using sorted function")