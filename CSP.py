import random

from Algorithm import Algorithm
from Board import Board


class CSP(Algorithm):
    def __init__(self):
        super().__init__()

    def solve(self, config):
        board = config
        conflicts_count = board.conflicts_count
        expanded_nodes = 0
        while conflicts_count > 0:
            i = random.sample(set(board.conflicting_queens), 1)[0]
            best, conflicts_count, passed, e = board.get_best_position(i)
            if not passed:
                e = board.random_move()
                conflicts_count = board.conflicts_count
                # print("Stuck, Random Choice!")
            else:
                board.move_queen(i, best)
            expanded_nodes += e
            # print('number of conflicts = ', conflicts_count, 'expanded nodes in this step = ', e ,' board = ', board._rows, '\n')


        return board, expanded_nodes
