import random

from Algorithm import Algorithm
from Board import Board


class Genetic(Algorithm):
    def __init__(self, n):
        super().__init__()
        self._generation_count = n

    def create_random_board(self):
        rows = []
        for i in range(0, 8):
            rand = random.randrange(8)
            rows.append(rand)
        board = Board()
        board.configure_with_queens(rows)
        return board

    def init_boards(self):
        boards = []
        for i in range(0, self._generation_count):
            board = self.create_random_board()
            boards.append(board)


    def solve(self, config):

        currentGeneration = self.init_states()









        pass
