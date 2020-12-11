#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(6)
    # Part 1
    answer_batches = [[]]
    for line in file_lines:
        if line == '':
            answer_batches.append([])
        else:
            answer_batches[-1].append(line)   
    
    answers = [''.join(batch) for batch in answer_batches]
    total_answers = sum(len(set(answer)) for answer in answers)
    print(f'Total number of yes answers: {total_answers}')
    
    # Part 2
    import collections
    
    single_groups = [batch for batch in answer_batches if len(batch) == 1]
    single_group_count = sum(len(''.join(group)) for group in single_groups)
    
    multi_groups = [batch for batch in answer_batches if len(batch) > 1]
    multi_group_answers = [[k for k, v in collections.Counter(''.join(group)).items() if v == len(group)] for group in multi_groups]
    multi_group_count = sum(len(''.join(group)) for group in multi_group_answers)
    
    print(f'Total number of yes answers: {single_group_count + multi_group_count}')
