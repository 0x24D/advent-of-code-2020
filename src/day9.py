#!/usr/bin/env python3

from common import read_file_to_int_list

if __name__ == '__main__':
    file_lines = read_file_to_int_list(9)
    # Part 1
    index = 25
    while index < len(file_lines):
        sum_count = 0
        for i in file_lines[index - 25 : index]:
            for j in file_lines[index - 25 : index]:
                if i != j and i + j == file_lines[index]:
                    sum_count += 1
        if sum_count == 0:
            break
        else:
            index += 1
    print(f"First number that isn't a sum from the previous 25: {file_lines[index]}")    
    
