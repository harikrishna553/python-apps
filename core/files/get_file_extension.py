import os

file_path = '/Users/Shared/poi/xls/test.xlsx'
file_name, file_extension = os.path.splitext(file_path)

print('file_name -> ', file_name)
print('file_extension -> ', file_extension)