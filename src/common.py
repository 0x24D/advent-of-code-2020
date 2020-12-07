#!/usr/bin/env python3

def read_file_to_int_list(n):
    with open(f'../inputs/day{n}.txt', 'r') as inputFile:
        file_lines = [int(line) for _, line in enumerate(inputFile)]
    return file_lines
            
