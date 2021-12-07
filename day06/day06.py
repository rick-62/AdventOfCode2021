# day03
import re
import sys

import numpy as np
from collections import Counter   
from math import ceil    


def convert_to_list(raw):
    return [int(x) for x in raw.split(',')]

def get_max_array_size(initial_list, days=80):
    '''Max numpy array size given the initial list and number of simulation days'''
    return len(initial_list) * 2 ** ceil(days / 7)

def init_numpy_array(initial_list, max_length):
    arr = np.full(max_length, 8, dtype=np.int8)
    for i, n in enumerate(initial_list):
        arr[i] = n
    pointer = i + 1
    return arr, pointer

def increment_one_day(arr, pointer):
    new = np.bincount(arr[:pointer])[0]
    arr[:pointer] -= 1
    arr[arr == -1] = 6
    pointer += new
    return arr, pointer

    
############
## PART 1 ##
############

# naive solution
def part1(raw, days=80):
    initial_list = convert_to_list(raw)
    mx = get_max_array_size(initial_list, days=days)
    arr, pointer = init_numpy_array(initial_list, mx)
    for n in range(1, days+1):
        arr, pointer = increment_one_day(arr, pointer)
    return pointer
       
############
## PART 2 ##
############

# non-naive solution
def part2(raw, days=256):

    initial_list = convert_to_list(raw)
    L = [0] * 9

    for i, x in Counter(initial_list).items():
        L[i] = x

    for n in range(1, days+1):
        C = L[1:9] + [L[0]]
        C[6] += L[0]
        L = C

    return sum(L)
                

if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').read()

    p1 = part1(raw_data)
    p2 = part2(raw_data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert p1 == 5934, p1
        assert p2 == 26984457539, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
