# day03
import re
import sys

import numpy as np
from collections import Counter, defaultdict   
from math import ceil    


def convert_to_lists(raw_data):
    for row in raw_data:
        yield [[frozenset(x) for x in row.split()] for row in  row.split(' | ')]



############
## PART 1 ##
############

def part1(raw):

    input_codes = convert_to_lists(raw)
    total_counts = Counter()

    for _, y in input_codes:
        total_counts += Counter([len(code) for code in y])

    return total_counts[3] + total_counts[4] + total_counts[7] + total_counts[2]
    


############
## PART 2 ##
############

def deduce_numbers(signals):

    lookup = [None] * 10

    # first pass
    for x in signals:
        l = len(x)
        if   l == 2: lookup[1] = x
        elif l == 3: lookup[7] = x
        elif l == 4: lookup[4] = x
        elif l == 7: lookup[8] = x

    # second pass
    for x in signals:
        l = len(x)
        if l == 6:
            if    lookup[4].issubset(x): lookup[9] = x
            elif  lookup[1].issubset(x): lookup[0] = x
            else: lookup[6] = x
        elif l == 5:
            if    lookup[1].issubset(x): lookup[3] = x
            elif  (lookup[4] - lookup[1]).issubset(x): lookup[5] = x
            else: lookup[2] = x

    return {x: str(i) for i, x in enumerate(lookup)}


def translate_codes(codes, lookup):
    return int(''.join([lookup[code] for code in codes]))


def part2(raw):

    input_codes = convert_to_lists(raw)
    total = 0

    for signals, codes in input_codes:
        lookup = deduce_numbers(signals)
        total += translate_codes(codes, lookup)
        
    return total

                

if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').readlines()

    p1 = part1(raw_data)
    p2 = part2(raw_data)

    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert p1 == 26, p1
        assert p2 == 61229, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
