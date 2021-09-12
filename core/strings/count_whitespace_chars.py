def count_whitespace_characters(str):
    count = 0
    for ch in str:
        if(ch.isspace() ==  True):
            count += 1
    return count

str1 = '   '
str2 = '\t\n\v\f\r'
str3 = ' hello \n how are you'
str4 = "hello"

print('Total whitespace characters in str1 ', count_whitespace_characters(str1))
print('Total whitespace characters in str2 ', count_whitespace_characters(str2))
print('Total whitespace characters in str3 ', count_whitespace_characters(str3))
print('Total whitespace characters in str4 ', count_whitespace_characters(str4))