# day03
import re
import sys

import numpy as np
from collections import Counter   
from math import ceil    


def convert_to_numpy_arr(raw):
    return np.array(raw.split(','), dtype=np.int16)

def calc_fuel(arr, position):
    return np.sum(np.abs(arr - position))

def triangular_func(n):
    return int(n*(n+1)/2)

def calc_accumulating_fuel(arr, position):
    triangular_vect = np.vectorize(triangular_func)
    return np.sum(triangular_vect(np.abs(arr - position)))


    
############
## PART 1 ##
############

def part1(raw):
    arr = np.sort(convert_to_numpy_arr(raw))
    previous = np.inf
    for position in range(max(arr)):
        cost = calc_fuel(arr, position)
        if cost > previous:
            break
        previous = cost
    return previous


############
## PART 2 ##
############

def part2(raw):
    arr = np.sort(convert_to_numpy_arr(raw))
    previous = np.inf
    for position in range(max(arr)):
        cost = calc_accumulating_fuel(arr, position)
        if cost > previous:
            break
        previous = cost
    return previous

                

if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').read()

    p1 = part1(raw_data)
    p2 = part2(raw_data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert calc_fuel(np.array([16,1,2,0,4,2,7,1,2,14]), 2) == 37
        assert calc_fuel(np.array([16,1,2,0,4,2,7,1,2,14]), 3) == 39
        assert calc_fuel(np.array([16,1,2,0,4,2,7,1,2,14]), 10) == 71
        assert p1 == 37, p1

        acc_fuel1 = calc_accumulating_fuel(np.array([1,2,3]), 2)
        acc_fuel2 = calc_accumulating_fuel(np.array([16,1,2,0,4,2,7,1,2,14]), 5)
        assert acc_fuel1 == 2, acc_fuel1
        assert acc_fuel2 == 168, acc_fuel2
        assert p2 == 168, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
