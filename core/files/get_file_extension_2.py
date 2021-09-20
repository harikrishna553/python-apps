import pathlib

file_path = '/Users/Shared/poi/xls/test.xlsx'
file_extension = pathlib.Path(file_path).suffix

print('file_extension -> ', file_extension)