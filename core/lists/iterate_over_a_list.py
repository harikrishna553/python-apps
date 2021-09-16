primes = [2, 3, 5, 7, 11]

primes_iterator = primes.__iter__()

while(True):
    try:
       next_ele =  primes_iterator.__next__()
       print(next_ele)
    except StopIteration:
        break