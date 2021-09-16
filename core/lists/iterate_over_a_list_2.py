primes = [2, 3, 5, 7, 11]

primes_iterator = iter(primes)

while(True):
    try:
       next_ele =  next(primes_iterator)
       print(next_ele)
    except StopIteration:
        break