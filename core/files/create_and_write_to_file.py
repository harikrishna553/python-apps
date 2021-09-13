import os

file_to_create = 'myfile.txt'

path = '/Users/Shared/data'
files_in_path = os.listdir(path) 

with open(os.path.join(path, file_to_create), 'w') as fp:    
    fp.write("Test line 1\n")
    fp.write("Test line 2")

with open(os.path.join(path, file_to_create), 'r') as fp:    
    file_content = fp.readlines()
    print(file_content)
