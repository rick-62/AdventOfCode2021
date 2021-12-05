# day03
import sys
import re
import numpy as np


def extract_draw_numbers(raw_data):
    return [int(x) for x in raw_data[0].split(',')]

def yield_game_board(raw_data):
    i = 2
    while raw_data[i:i+5]:
        yield np.genfromtxt(raw_data[i:i+5], dtype=np.uint16)
        i += 6

class Board():

    def __init__(self, game_board) -> None:
        self.numbers_drawn = set()
        self.lines = self._extract_rows_and_columns(game_board)
    
    @staticmethod
    def _extract_rows_and_columns(game_board: np.array) -> None:
        rows = [frozenset(row) for row in game_board]
        columns = [frozenset(col) for col in zip(*game_board)]
        return frozenset(rows + columns)

    def draw(self, number):
        self.numbers_drawn.add(number)

    @property   
    def is_winner(self):
        for line in self.lines:
            if line.issubset(self.numbers_drawn):
                return True
    
    @property
    def sum_unmarked(self):
        return int(sum(sum(line - self.numbers_drawn) for line in self.lines) / 2)

        
############
## PART 1 ##
############

def part1(raw_data):
    game_boards = [Board(board) for board in yield_game_board(raw_data)]
    for number in extract_draw_numbers(raw_data):
        for board in game_boards:
            board.draw(number)
            if board.is_winner:
                return board.sum_unmarked * number
       
############
## PART 2 ##
############

def part2(data):
    game_boards = [Board(board) for board in yield_game_board(raw_data)]
    for number in extract_draw_numbers(raw_data):
        for board in game_boards.copy():
            board.draw(number)
            if board.is_winner and len(game_boards) > 1:
                game_boards.remove(board)
            elif board.is_winner:
                return board.sum_unmarked * number

                

if __name__ == '__main__':

    print(sys.argv[0])

    file_name = 'test.txt' if sys.argv[-1] == 'test' else 'input.txt'

    raw_data = open(file_name, 'r').readlines()

    p1 = part1(raw_data)
    p2 = part2(raw_data)
    
    if sys.argv[-1] == 'test':
        print("Testing...")
        game_boards = [board for board in yield_game_board(raw_data)]
        first_board = Board(game_boards[0])
        second_board = Board(game_boards[1])
        last_board = Board(game_boards[-1])
        assert len(first_board.lines) == 10
        assert len(last_board.lines) == 10
        assert len(second_board.lines) == 10
        assert not first_board.is_winner
        assert first_board.sum_unmarked == 300, first_board.sum_unmarked
        assert len(game_boards) == 3
        assert len(extract_draw_numbers(raw_data)) == 27
        assert p1 == 4512, p1
        assert p2 == 1924, p2

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    
