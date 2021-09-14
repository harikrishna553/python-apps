str1 = 'Hi, I am {} and {} years old. I am from {}'.format('Krishna', 31, 'India')
str2 = 'Hi, I am {1} and {0} years old. I am from {2}'.format( 31, 'Krishna', 'India')
str3 = 'Hi, I am {name} and {age} years old. I am from {country}'.format( age=31, name='Krishna', country='India')

print(str1)
print(str2)
print(str3)