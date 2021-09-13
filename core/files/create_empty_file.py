import os

file_to_create = 'myfile.txt'

path = '/Users/Shared/data'
files_in_path = os.listdir(path) 
print("List of directories and files before creating ", file_to_create)
print(files_in_path)

with open(os.path.join(path, file_to_create), 'w') as fp:    
    pass

files_in_path = os.listdir(path) 
print("List of directories and files after creating ", file_to_create)
print(files_in_path)