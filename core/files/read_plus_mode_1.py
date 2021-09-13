import os

file_to_check = 'hello.txt'
path = "/Users/Shared/data"

with open(os.path.join(path, file_to_check), 'r+') as fp:
    lines = fp.readlines() 
    print(lines)

    print("\nWriting some content to the file\n")

    # Placing the file handle to start
    fp.seek(0)
    fp.write("test 1\n")

    # Placing the file handle to start
    fp.seek(0)
    lines = fp.readlines()
    print(lines)
