import os
import shutil

source_file_1 = '/Users/Shared/test/p1/p1_1/a.txt'
dest_file_1 = '/Users/Shared/test/p1/p1_2/a.txt'
os.rename(source_file_1, dest_file_1)

source_file_2 = '/Users/Shared/test/p2/p2_1/a.txt'
dest_file_2 = '/Users/Shared/test/p2/p2_2/a.txt'
shutil.move(source_file_2, dest_file_2)
