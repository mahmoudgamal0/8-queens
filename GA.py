import random

from Algorithm import Algorithm
from Board import Board


class Genetic(Algorithm):
    def __init__(self, n):
        super().__init__()
        self._generation_count = n
        self.explored_set = {}
        self.expanded_nodes = 0
        self._cost = 0

    def create_random_board(self):
        rows = []
        #while True:
        for i in range(0, 8):
            rand = random.randrange(8)
            rows.append(rand)
            if tuple(rows) not in self.explored_set:
                self.expanded_nodes += 1
            else:
                self.explored_set[tuple(rows)] = True
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
                return boards, generation_lottery, True
            for j in range(0, 28 -int(board.conflicts_count)):
                generation_lottery.append(i)
        if len(generation_lottery) > self._generation_count:
            return boards, generation_lottery, False
        return self.init_boards()

    def mutate_board(self, board):
        board.move_queen(random.randrange(8), random.randrange(8))
        
    def solve(self, config):
        current_generation, generation_lottery, found_solution = self.init_boards()
        self.cost = 1
        current_generation[len(current_generation) - 1].cost = self.cost
        if found_solution:
            return current_generation[len(current_generation) - 1], self.expanded_nodes
        while not found_solution:
            current_generation, generation_lottery, found_solution = \
                self.get_new_generation(current_generation, generation_lottery)
            self.cost += 1
            if found_solution:
                current_generation[len(current_generation) - 1].cost = self.cost
                return current_generation[len(current_generation) - 1], self.expanded_nodes




    def select_board(self, boards, generation_lottery):
        return boards[random.choice(generation_lottery)]


    def merge_boards(self, b1, b2):
        board = Board()
        split_point = random.randrange(8)
        row1 = b1._rows
        row2 = b2._rows
        new_row = [row1[i] if i <= split_point else row2[i] for i in range(0, 8)]
        board.configure_with_queens(new_row)
        return board

    def get_new_generation(self, boards, generation_lottery):
        new_boards = []
        new_generation_lottery = []
        for i in range(0, self._generation_count):
            board1 = self.select_board(boards, generation_lottery)
            board2 = self.select_board(boards, generation_lottery)
            board = self.merge_boards(board1, board2)
            while random.uniform(0, 1) < 0.2:
                self.mutate_board(board)
            # print(board._rows)
            rows = board._rows
            if tuple(rows) not in self.explored_set:
                self.expanded_nodes += 1
            else:
                self.explored_set[tuple(rows)] = True
            new_boards.append(board)
            if board.conflicts_count == 0:
                return new_boards, new_generation_lottery, True
            for j in range(0, 28 - int(board.conflicts_count)):
                new_generation_lottery.append(i)
        return new_boards, new_generation_lottery, False
