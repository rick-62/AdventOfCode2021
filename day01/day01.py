# day01
import sys
import numpy as np  # v1.20+

from numpy.lib.stride_tricks import sliding_window_view


def part1(data):
    return np.sum(np.diff(data) >= 1)

def part2(data):
    return part1(np.sum(sliding_window_view(data, window_shape=3), axis=1))

    
if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').readlines()
    data = np.array([int(row.strip('\n')) for row in raw_data])

    p1 = part1(data)
    p2 = part2(data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert p1 == 7, p1
        assert p2 == 5, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
