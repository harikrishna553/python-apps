def arith(a, b):
    result = dict()

    result['sum'] = a + b
    result['sub'] = a - b
    result['mul'] = a * b
    result['div'] = a / b

    return result

result_dict = arith(10, 2)

print('sum of 10 and 2 is ', result_dict['sum'])
print('subtract of 10 and 2 is ', result_dict['sub'])
print('multiplication of 10 and 2 is ', result_dict['mul'])
print('Division of 10 and 2 is ', result_dict['div'])
