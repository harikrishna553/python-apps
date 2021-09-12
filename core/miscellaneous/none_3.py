def is_none(x, variable_name):
    if x == None:
        print(variable_name, ' is set to None')
    else:
        print(variable_name, ' is not None')

a = None
b = False
c = 0
d = ""
e = 0.00

is_none(a, 'a')
is_none(b, 'b')
is_none(c, 'c')
is_none(d, 'd')
is_none(e, 'e')