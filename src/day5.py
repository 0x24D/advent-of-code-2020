#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(5)
    # Part 1
    seat_ids = []
    for line in file_lines:
        row_range = [value for value in range(0, 128)]
        col_range = [value for value in range(0, 8)]
        for char in line:
            if char == 'F':
                row_range = row_range[:len(row_range)//2]
            elif char == 'B':
                row_range = row_range[len(row_range)//2:]
            elif char == 'L':
                col_range = col_range[:len(col_range)//2]
            else:
                col_range = col_range[len(col_range)//2:]
        seat_ids.append((row_range[0] * 8) + col_range[0])
    seat_ids.sort()
    print(f'Highest seat ID: {seat_ids[len(seat_ids) - 1]}')

    # Part 2
    for i in range(0, len(seat_ids), 2):
        if seat_ids[i + 1] - seat_ids[i] == 2:
            print(f'Seat ID: {seat_ids[i] + 1}')
            break
