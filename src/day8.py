#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(8)
    # Part 1
    ic = 0
    acc = 0
    used_instructions = []
    while ic <= len(file_lines):
        if ic in used_instructions:
            break
        else:
            used_instructions.append(ic)
        instructions = file_lines[ic].split(' ')
        if instructions[0] == 'jmp':
            ic += int(instructions[1])
        else:
            if instructions[0] == 'acc':
                acc += int(instructions[1])
            ic += 1
    print(f'Accumulator value before second instruction run: {acc}')
    
