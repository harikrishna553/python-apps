import os

file_to_read = 'myfile.txt'
path = '/Users/Shared/data'

with open(os.path.join(path, file_to_read), 'r') as fp:
    no_of_lines = len(fp.readlines())
    print('Number of lines in a file : ', no_of_lines)