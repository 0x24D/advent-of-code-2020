#!/usr/bin/env python3

from common import read_file_to_int_list

if __name__ == '__main__':
    file_lines = read_file_to_int_list(10)
    # Part 1
    file_lines.sort()
    print(file_lines)
    joltage = 0
    jump1 = jump3 = 0
    while joltage != file_lines[-1] + 3:
        if joltage + 1 in file_lines:
            joltage += 1
            jump1 += 1
        elif joltage +2 in file_lines:
            joltage += 2
        else:
            joltage += 3
            jump3 += 1

    print(f'Number of 1-jolt differences * number of 3-jolt differences: {jump1 * jump3}')
