import os

def get_specific_line(file_path, line_number):
    count = 0
    
    with open(file_path) as fp:
        for line in fp:
            count += 1
            if(count == line_number):
                return line

path = '/Users/Shared/data/myfile.txt'

print(get_specific_line(path, 2).strip())
print(get_specific_line(path, 20))


