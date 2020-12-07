#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(2)
    # Part 1
    valid_passwords = 0
    for split_line in [line.split(' ') for line in file_lines]:
        char_count = split_line[2].count(split_line[1].replace(':', ''))
        char_range = [int(number) for number in split_line[0].split('-')]
        if char_count >= char_range[0] and char_count <= char_range[1]:
            valid_passwords += 1
    print(f'Number of valid passwords: {valid_passwords}')

    # Part 2
    valid_passwords = 0
    for split_line in [line.split(' ') for line in file_lines]:
        char = split_line[1].replace(':', '')
        char_positions = [int(number) for number in split_line[0].split('-')]
        password = split_line[2]
        # XOR
        if (password[char_positions[0] - 1] == char and (not password[char_positions[1] - 1] == char)) or ((not password[char_positions[0] - 1] == char) and password[char_positions[1] - 1] == char):
            valid_passwords += 1
    print(f'Number of valid passwords: {valid_passwords}')
    
