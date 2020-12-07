#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(3)
    # Part 1
    slope = (3,1)
    gradient = slope[0] / slope[1]
    row_len = len(file_lines[0])
    column_len = len(file_lines)
    repeats = 0
    while row_len * repeats < gradient * column_len:
        repeats += 1    
    extended_map = [line * repeats for line in file_lines]
    x, y = 0, 0
    trees_encountered = 0
    while y < len(extended_map):
        if extended_map[y][x] == '#':
            trees_encountered += 1
        x += slope[0]
        y += slope[1]
    print(f'Trees encountered: {trees_encountered}')
    
    # Part 2
    trees_encountered_multiplied = 1
    for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        gradient = slope[0] / slope[1]
        row_len = len(file_lines[0])
        column_len = len(file_lines)
        repeats = 0
        while row_len * repeats < gradient * column_len:
            repeats += 1    
        extended_map = [line * repeats for line in file_lines]
        x, y = 0, 0
        trees_encountered = 0
        while y < len(extended_map):
            if extended_map[y][x] == '#':
                trees_encountered += 1
            x += slope[0]
            y += slope[1]
        trees_encountered_multiplied *= trees_encountered
    print(f'Trees encountered multiplied: {trees_encountered_multiplied}')
