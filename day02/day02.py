# day02
import sys
import numpy as np

class Submarine:
    
    def __init__(self, operations):
        self.operations = operations
        self.coord = {
            'h': 0,  # horizontal
            'd': 0,  # depth
            'a': 0,  # aim
        }

    def command(self, text: str) -> None:
        direction, x = text.split(' ')
        fn = self.operations[direction]
        self.coord.update(fn(int(x), **self.coord))

    def multiply_coords(self) -> int:
        return self.coord['h'] * self.coord['d']


def part1(data):

    submarine = Submarine({
        'forward':  lambda x,h,**k: {'h': h+x},
        'down':     lambda x,d,**k: {'d': d+x},
        'up':       lambda x,d,**k: {'d': d-x},
    })

    for line in data:
        submarine.command(line)
    return submarine.multiply_coords()


def part2(data):

    submarine = Submarine({
        'forward':  lambda x,h,d,a,**k: {'h': h+x, 'd': d+a*x},
        'down':     lambda x,a,**k: {'a': a+x},
        'up':       lambda x,a,**k: {'a': a-x},
    })

    for line in data:
        submarine.command(line)
    return submarine.multiply_coords()



    
if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').readlines()
    data = np.array([row.strip('\n') for row in raw_data])

    p1 = part1(data)
    p2 = part2(data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        assert p1 == 150, p1
        assert p2 == 900, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
