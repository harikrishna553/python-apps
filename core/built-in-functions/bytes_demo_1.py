message = 'Hello World'

# convert string to bytes
byte_message1 = bytes(message, 'utf-8')
byte_message2 = bytes(message, 'utf-16')
byte_message3 = bytes(message, 'utf-32')

print('byte_message1 -> ', byte_message1, 'len(byte_message1) ' , len(byte_message1))
print('byte_message2 -> ', byte_message2, 'len(byte_message2) ' , len(byte_message2))
print('byte_message3 -> ', byte_message3, 'len(byte_message3) ' , len(byte_message3))