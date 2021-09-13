import os

file_to_read = 'hello.txt'
path = "/Users/Shared/data"

with open(os.path.join(path, file_to_read), 'r') as fp:
    lines = fp.readlines()      
    print(lines)
