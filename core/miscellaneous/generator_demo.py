def send_messge():
    print('about to yield "Hello"')
    yield 'Hello'

    print('about to yield "Hi"')
    yield 'Hi'

    print('about to yield "are you there"')
    yield 'are you there'

state = send_messge()

# yields the result of first yield statement
print('calling the next method first time')
print (next(state))

# yields the result of second yield statement
print('\ncalling the next method second time')
print (next(state))

# yields the result of third yield statement
print('\ncalling the next method third time')
print (next(state))