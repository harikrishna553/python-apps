import os

file_path = '/Users/Shared/poi/xls/abc_org.xls'
size_in_bytes = os.path.getsize(file_path)

print('file size : ', size_in_bytes, ' bytes')