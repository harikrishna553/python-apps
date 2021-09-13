def get_specific_lines(file_path, line_numbers):
    count = 0

    result = dict()
    
    with open(file_path) as fp:
        for line in fp:
            count += 1
            if(count in line_numbers):
                result[count] = line.strip()
    return result

path = '/Users/Shared/data/myfile.txt'

print(get_specific_lines(path, [2, 4, 5]))


