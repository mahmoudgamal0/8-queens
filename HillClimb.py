import copy
import random

from Algorithm import Algorithm


class HillClimb(Algorithm):
    def __init__(self):
        super().__init__()

    def solve(self, config):
        board = config
        conflicts_count = board.conflicts_count
        path = []
        explored_nodes = 0
        while conflicts_count > 0:
            best_queens, min_queens = [], []
            for queen in range(0, 8):
                best, minimum, passed, explored = board.get_best_position(queen)
                best_queens.append(best)
                min_queens.append(minimum)
                explored_nodes += explored

            min_conflicts = conflicts_count
            min_successor = []
            best_successor = []
            queen = []
            for index, (best, minimum) in enumerate(zip(best_queens, min_queens)):
                if minimum <= min_conflicts:
                    min_successor.append(minimum)
                    best_successor.append(best)
                    queen.append(index)
                    min_conflicts = minimum

            if len(min_successor) == 0:
                # Local Max
                board.random_move()
                path.append(copy.deepcopy(board.config))
                conflicts_count += board.conflicts_count
                continue

            # Get Unique minimum
            unique_min = self._get_unique_index(min_successor)
            if unique_min == -1:
                # Shoulder
                unique_min = random.randrange(len(queen))

            board.move_queen(queen[unique_min], best_successor[unique_min])
            path.append(copy.deepcopy(board.config))
            conflicts_count = min_successor[unique_min]

        return board, explored_nodes, path

    def _get_unique_index(self, items):
        if len(items) == 0:
            return -1
        min_item = min(items)
        min_count = items.count(min_item)
        if min_count > 1:
            return -1
        return items.index(min_item)
