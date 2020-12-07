#!/usr/bin/env python3

from common import read_file_to_int_list

if __name__ == '__main__':
    file_lines = read_file_to_int_list(1)
    # Part 1
    for c, l in enumerate(file_lines):
        for c2, l2 in enumerate(file_lines):
            if c == c2:
                pass
            else:
                if l + l2 == 2020:
                    print(f'{l}*{l2}={l*l2}')
                    break
    # Part 2
    for c, l in enumerate(file_lines):
        for c2, l2 in enumerate(file_lines):
            for c3, l3 in enumerate(file_lines):
                if c == c2 and c == c3:
                    pass
                else:
                    if l + l2 + l3 == 2020:
                        print(f'{l}*{l2}*{l3}={l*l2*l3}')
                        break
    
