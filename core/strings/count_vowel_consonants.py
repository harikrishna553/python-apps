def count_vowels_and_consonants(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']

    vowels_count = 0
    consonants_count = 0
    
    for ch in input_str:
        if ch.lower() in vowels:
            vowels_count += 1
        elif ( (ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
            consonants_count += 1
    return (vowels_count, consonants_count)

(vowels_count, consonants_count) = count_vowels_and_consonants('Hello WOrld')

print('vowels_count -> ', vowels_count)
print('consonants_count -> ', consonants_count)