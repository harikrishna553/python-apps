import os

file_to_read = 'myfile.txt'
path = '/Users/Shared/data'

with open(os.path.join(path, file_to_read), 'r') as fp:
    for line in fp:
        print("{}".format(line.strip()))

