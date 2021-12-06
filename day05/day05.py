# day03
import re
import sys

import numpy as np
from itertools import product
from collections import defaultdict


def extract_coordinates(raw_data):
    return (map(int, re.split(r'\W+', x.strip('\n'))) for x in raw_data)

def get_coordinate_ranges(x1, y1, x2, y2):
    rx = range(x1, x2-1, -1) if x1 > x2 else range(x1, x2+1)
    ry = range(y1, y2-1, -1) if y1 > y2 else range(y1, y2+1)
    return rx, ry

def extract_points(*coords):
    rx, ry = get_coordinate_ranges(*coords)
    if len(rx) == 1 or len(ry) == 1:
        return product(rx, ry)  # straight lines
    else:
        return zip(rx, ry)  # diagonal lines

# debugging
def print_test_array(d, n=10):
    M = np.zeros(shape=(n, n), dtype=str)
    M[tuple(zip(*d.keys()))] = list(d.values())
    M[M==''] = '.'
    for line in M.transpose():
        print(' '.join(map(str, line)))
        

     
############
## PART 1 ##
############

def part1(raw_data):
    floor = defaultdict(lambda:0)
    for x1, y1, x2, y2 in extract_coordinates(raw_data):
        if (x1 != x2) and (y1 != y2):
            continue
        for coord in extract_points(x1, y1, x2, y2):
            floor[coord] += 1
    return len([v for v in floor.values() if v > 1])

       
############
## PART 2 ##
############

def part2(data):
    floor = defaultdict(lambda:0)
    for x1, y1, x2, y2 in extract_coordinates(raw_data):
        for coord in extract_points(x1, y1, x2, y2):
            floor[coord] += 1
    # print_test_array(floor)
    return len([v for v in floor.values() if v > 1])

                

if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').readlines()

    p1 = part1(raw_data)
    p2 = part2(raw_data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert set(extract_points(9,4,3,4)) == {(6, 4), (5, 4), (4, 4), (7, 4), (9, 4), (3, 4), (8, 4)}, set(extract_points(9,4,3,4))
        assert set(extract_points(1,1,2,2)) == {(1, 1), (2, 2)}, set(extract_points(1,1,2,2))
        assert set(extract_points(5,5,8,2)) == {(5, 5), (6, 4), (7, 3), (8, 2)}, set(extract_points(5,5,8,2))
        assert p1 == 5, p1
        assert p2 == 12, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
