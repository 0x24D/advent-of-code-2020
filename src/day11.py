#!/usr/bin/env python3

from common import read_file_to_str_list
from copy import deepcopy

if __name__ == '__main__':
    file_lines = read_file_to_str_list(11)
    # Part 1
    seat_map = [list(r) for r in file_lines]
    s_max = len(seat_map[0]) - 1
    r_max = len(seat_map) - 1
    while True:
        number_of_changes = 0
        read_map = deepcopy(seat_map)
        for r, row in enumerate(read_map):
            for s, seat in enumerate(row):
                occupied_seats = 0
                if seat == 'L' or seat == '#':
                    if s != 0 and read_map[r][s - 1] == '#': # West
                        occupied_seats += 1
                    if s != s_max and read_map[r][s + 1] == '#': # East
                        occupied_seats += 1
                    if r != 0 and read_map[r - 1][s] == '#':  # North
                        occupied_seats += 1
                    if r != r_max and read_map[r + 1][s] == '#': # South
                        occupied_seats += 1
                    if s != 0 and r != 0 and read_map[r - 1][s - 1] == '#': # NW
                        occupied_seats += 1
                    if s != s_max and r != 0 and read_map[r - 1][s + 1] == '#': # NE
                        occupied_seats += 1
                    if s != s_max and r != r_max and read_map[r + 1][s + 1] == '#': # SE
                        occupied_seats += 1
                    if s != 0 and r != r_max and read_map[r + 1][s - 1] == '#': # SW
                        occupied_seats += 1
                    if seat == 'L' and occupied_seats == 0:
                        seat_map[r][s] = '#'
                        number_of_changes += 1
                    elif seat == '#' and occupied_seats >= 4:
                        seat_map[r][s] = 'L'
                        number_of_changes += 1
        if number_of_changes == 0:
            break
    print(f"Number of occupied seats after all changes: {sum([r.count('#') for r in seat_map])}")
