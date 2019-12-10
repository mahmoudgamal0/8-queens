import random

from Algorithm import Algorithm
from Board import Board


class Genetic(Algorithm):
    def __init__(self, n):
        super().__init__()
        self._generation_count = n
        self.explored_set = {}

    def create_random_board(self):
        rows = []
        #while True:
        for i in range(0, 8):
            rand = random.randrange(8)
            rows.append(rand)
            #if tuple(rows) in self.explored_set:

        board = Board()
        board.configure_with_queens(rows)
        return board

    def init_boards(self):
        boards = []
        generation_lottery = []
        for i in range(0, self._generation_count):
            board = self.create_random_board()
            boards.append(board)
            if board.conflicts_count == 0:
                return boards
            for j in range(0, 28 - board.conflicts_count):
                generation_lottery.append(i)
        if len(generation_lottery) > self._generation_count:
            return boards, generation_lottery
        return self.init_boards()

    def mutate_board(self, board):
        board.move_queen(random.randrange(8), random.randrange(8))

    def solve(self, config):
        current_generation, generation_lottery, found_solution = self.init_boards()
        if found_solution:
            return current_generation[len(current_generation) - 1]
        while True:
            current_generation, generation_lottery, found_solution = \
                self.get_new_generation(current_generation, generation_lottery)

    def select_board(self,boards,generation_lottery):
        return boards[random.choice(generation_lottery)]

    def get_new_generation(self, boards, generation_lottery):
        boards = []
        generation_lottery = []
        for i in range(0, self._generation_count):
            board1 = self.select_board(boards, generation_lottery)
            board2 = self.select_board(boards, generation_lottery)
            split_point = random.randrange(8)

            #
            # boards.append(board)
            # if board.conflicts_count == 0:
            #     return boards
            # for j in range(0, 28 - board.conflicts_count):
            #     generation_lottery.append(i)
