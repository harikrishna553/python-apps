vowels = {'a', 'e', 'i', 'o', 'u'}
fset = frozenset(vowels)

print('vowels : ', vowels)
print('fset : ', fset)

vowels.remove('e')
print('vowels : ', vowels)

fset.remove('e')
print('fset : ', fset)
