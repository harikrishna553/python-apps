def upper_lower_conversion(str):
    chars = list(str)
    result = []

    for ch in str:
        if ch.isupper():
            result.append(ch.lower())
        elif ch.islower():
            result.append(ch.upper())
        else:
            result.append(ch)
    
    return ''.join(result)

str1 = 'HeLLo WoRLd'
converted_str = upper_lower_conversion(str1)

print('str1 -> ', str1)
print('converted_str -> ', converted_str)