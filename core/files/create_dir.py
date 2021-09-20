import os

def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
        print('Directory created successfully!!!')
    except FileExistsError:
        print('File with given name ', dir_path, ' is already exists')
 

create_dir('/Users/Shared/poi/xls/test1')
create_dir('/Users/Shared/poi/xls/test1')