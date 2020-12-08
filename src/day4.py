#!/usr/bin/env python3

from common import read_file_to_str_list

if __name__ == '__main__':
    file_lines = read_file_to_str_list(4)
    # Part 1
    passport_batches = [[]]
    i = 0
    for line in file_lines:
        if line == '':
            i += 1
            passport_batches.append([])
        else:
            passport_batches[i].append(line)
    valid_passports = 0
    for batch in passport_batches:
        passport_fields = [pair.split(':')[0] for pair in ' '.join(batch).split(' ')]
        if all(field in passport_fields for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            valid_passports +=1
    print(f'Number of valid passports: {valid_passports}')
    
    # Part 2
    passport_batches = [[]]
    i = 0
    for line in file_lines:
        if line == '':
            i += 1
            passport_batches.append([])
        else:
            passport_batches[i].append(line)
    valid_passports = 0
    for batch in passport_batches:
        passport_fields = [pair.split(':') for pair in ' '.join(batch).split(' ')]
        valid_fields = 0
        for field in passport_fields:
            if field[0] == 'byr' and len(field[1]) == 4:
                byr = int(field[1])
                if byr >= 1920 and byr <= 2002:
                    valid_fields += 1
            elif field[0] == 'iyr' and len(field[1]) == 4:
                iyr = int(field[1])
                if iyr >= 2010 and iyr <= 2020:
                    valid_fields += 1
            elif field[0] == 'eyr' and len(field[1]) == 4:
                eyr = int(field[1])
                if eyr >= 2020 and eyr <= 2030:
                    valid_fields += 1
            elif field[0] == 'hgt' and len(field[1]) > 2:
                m = field[1][-2:]
                hgt = int(field[1][:-2])
                if m == 'cm' and hgt >= 150 and hgt <= 193 or m == 'in' and hgt >= 59 and hgt <= 76:
                    valid_fields += 1
            elif field[0] == 'hcl' and len(field[1]) == 7 and field[1][:1] == '#':
                try:
                    int(field[1][1:], 16)
                except ValueError: # Contains a non-hex value
                    continue
                valid_fields += 1
            elif field[0] == 'ecl' and field[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid_fields += 1
            elif field[0] == 'pid' and len(field[1]) == 9:
                try:
                    int(field[1])
                except ValueError: # Contains a non-numeric value
                    continue
                valid_fields += 1
        if valid_fields == 7:
            valid_passports += 1
    print(f'Number of valid passports: {valid_passports}')
    
