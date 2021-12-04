# day03
import sys
import numpy as np


def convert_bin_array_to_int(arr):
    return int(''.join([str(x) for x in arr]), 2)

############
## PART 1 ##
############

def part1(data):
    cnt_ones = np.sum(data, axis=0)
    gamma_array = (cnt_ones > len(data)/2).astype(np.int0)
    gamma = convert_bin_array_to_int(gamma_array)
    epsilon = gamma ^ (2**len(cnt_ones)-1)
    return gamma * epsilon


############
## PART 2 ##
############

def filter_binary(data, rating, i=0):

    if len(data) == 1:
        return convert_bin_array_to_int(data[0])

    cnt_ones = np.sum(data[:,i], axis=0)
    cnt_zeroes = len(data) - cnt_ones

    if rating == 'oxygen_generator':
        if cnt_ones >= cnt_zeroes:
            new_data = data[np.where(data[:,i] == 1)]
        else:
            new_data = data[np.where(data[:,i] == 0)]

    elif rating == 'CO2_scrubber':
        if cnt_ones < cnt_zeroes:
            new_data = data[np.where(data[:,i] == 1)]
        else:
            new_data = data[np.where(data[:,i] == 0)]

    else:
        raise Exception(f"rating is not acceptable argument")
    
    return filter_binary(new_data, rating, i+1)


def part2(data):
    oxygen_generator = filter_binary(data, rating='oxygen_generator')
    CO2_scrubber = filter_binary(data, rating='CO2_scrubber')
    return oxygen_generator * CO2_scrubber


if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').readlines()
    data = np.array([list(int(x) for x in row.strip('\n')) for row in raw_data])

    p1 = part1(data)
    p2 = part2(data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert p1 == 198, p1
        assert filter_binary(data, rating='oxygen_generator') == 23
        assert filter_binary(data, rating='CO2_scrubber') == 10, filter_binary(data, rating='CO2_scrubber')
        assert p2 == 230, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
