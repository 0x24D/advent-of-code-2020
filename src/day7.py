#!/usr/bin/env python3

from common import read_file_to_str_list
import re

if __name__ == '__main__':
    file_lines = read_file_to_str_list(7)
    """
    file_lines = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
                    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
                    'bright white bags contain 1 shiny gold bag.',
                    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
                    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
                    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
                    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
                    'faded blue bags contain no other bags.',
                    'dotted black bags contain no other bags.']
    """
    # Part 1
    def get_bags_that_contain(bag_colour):
        bags = []
        for line in file_lines:    
            matches = re.findall(f'.*contains*.*{bag_colour} bags*.*', line)
            if matches != []:
                matches = re.findall('.*bags contains*', matches[0])
                bags.append(matches[0][:matches[0].find(' ', matches[0].find(' ') + 1)])
        return bags

    bags = ['shiny gold']
    all_bags = []
    count = 0
    while True:
        temp = []
        for bag in bags:
            temp += get_bags_that_contain(bag)
        if temp == []:
            break
        else:
            bags = temp
            all_bags += temp
    print(f'Total number of bags containing shiny gold: {len(set(all_bags))}')

    # Part 2
    def get_bags_that_are_in(bag_colour):
        bags = []
        for line in file_lines:    
            matches = re.findall(f'^{bag_colour}.*', line)
            if matches != [] and 'contain no other bags' not in matches[0]:
                matches = re.findall('contains*.*', matches[0])
                bags_contained = ''.join(matches[0][matches[0].find(' ') + 1:]).split(',')
                for bag in bags_contained:
                    bag = bag.strip()
                    first_space = bag.find(' ') + 1
                    num_bags = int(bag[:first_space])
                    colour = bag[first_space: len(bag) - bag[::-1].find(' ') - 1]
                    bags.append((bag_colour, colour, num_bags))
        return bags
    """
    bags = ['shiny gold']
    all_bags = []
    count = 0
    while True:
        temp = []
        for bag in bags:
            temp += get_bags_that_are_in(bag)
        if temp == []:
            break
        else:
            bags = [t[1] for t in temp]
            all_bags += temp
    print(all_bags)
    
    # outer_bag, inner_bag, num_inner_bags
    
    bags = [bag for bag in all_bags if bag[0] == 'shiny gold']
    print(bags)
    for b in bags:
        inner_bags = [bag for bag in all_bags if bag[0] == b[1]]
        print(inner_bags)
    """
