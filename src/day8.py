#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(8)
    # Part 1
    ic = 0
    acc = 0
    used_instructions = []
    while ic < len(file_lines):
        if ic in used_instructions:
            break
        else:
            used_instructions.append(ic)

        instruction = file_lines[ic].split(' ')
        if instruction[0] == 'jmp':
            ic += int(instruction[1])
        else:
            if instruction[0] == 'acc':
                acc += int(instruction[1])
            ic += 1
    print(f'Accumulator value before second instruction run: {acc}')
    
    # Part 2
    jmp_or_nop = True # jmp = True, nop = False
    num_to_change = 0
    num_jmps = len([j for j in file_lines if j.startswith('jmp')])
    while True:
        ic = 0
        acc = 0
        used_instructions = []
        jmp_nop_visited = 0
        while ic < len(file_lines):
            if ic in used_instructions:
                if jmp_or_nop and num_to_change == num_jmps:
                    jmp_or_nop = False
                    num_to_change = 0
                else:
                    num_to_change += 1
                break
            else:
                used_instructions.append(ic)

            instruction = file_lines[ic].split(' ')
            if instruction[0] == 'jmp' or instruction[0] == 'nop':
                if jmp_or_nop and instruction[0] == 'jmp':
                    jmp_nop_visited += 1
                    if jmp_nop_visited == num_to_change:
                        instruction[0] = 'nop'
                elif not jmp_nop_visited and instruction[0] == 'nop':
                    jmp_nop_visited += 1
                    if jmp_not_visited == num_to_change:
                        instruction[0] = 'jmp'

            if instruction[0] == 'jmp':
                ic += int(instruction[1])
            else:
                if instruction[0] == 'acc':
                    acc += int(instruction[1])
                ic += 1
        
        if ic == len(file_lines):
            break
    print(f'Accumulator value after terminating program: {acc}')
    
