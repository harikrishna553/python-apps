msg = 'My age is ';
age = 32

str1 = msg + str(age)
print(str1)

str2 = "%s%s" % (msg, age)
print(str2)

str3 = "{}{}".format(msg, age)
print(str3)

str4 = f'{msg}{age}'
print(str4)