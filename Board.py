class Board:
    def __init__(self):
        self._config = []
        self.conflicting_queens = {}
        self.conflicts_count = 0
        self.rows = []

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        board_list = value.split('\n')
        board_list = [elem.split(' ') for elem in board_list]
        self._config = []
        for line in board_list:
            row = [1 if elem == 'Q' else 0 for elem in line]
            self._config.append(row)
        # TODO each column one queen

        rows_of_queens = []
        for j in range(0, 8):
            rows_of_queens.append(([i for i in range(0, 8) if self.config[i][j] == 1])[0])
        self.rows = rows_of_queens
        self.set_conflicting_pairs()

    def solve(self, algorithm):
        algorithm.solve(self._config)

    def set_conflicting_pairs(self):
        rows_of_queens = self.rows
        conflicting_queens = set()
        conflicts_count = 0
        queens_count_in_row = [0 for i in range(0, 8)]
        queen_indexes = [[] for i in range(0, 8)]
        for i in range(0, 8):
            queens_count_in_row[rows_of_queens[i]] += 1
            queen_indexes[rows_of_queens[i]].append(i)

        for i in range(0, 8):
            if queens_count_in_row[i] > 1:
                conflicts_count += queens_count_in_row[i]*(queens_count_in_row[i] - 1) / 2
                for index in queen_indexes[i]:
                    conflicting_queens.add(index)

        queen_indexes = [[] for i in range(0, 14)]
        queens_count_in_main_diag = [0 for i in range(0, 8)]

        for i in range(0, 8):
            s = rows_of_queens[i] + i
            queens_count_in_main_diag[s] += 1
            queen_indexes[s].append(i)

        for i in range(0, 14):
            if queens_count_in_main_diag[i] > 1:
                conflicts_count += queens_count_in_main_diag[i]*(queens_count_in_main_diag[i] - 1) / 2
                for index in queen_indexes[i]:
                    conflicting_queens.add(index)

        queen_indexes = [[] for i in range(0, 14)]
        queens_count_in_sec_diag = [0 for i in range(0, 8)]

        for i in range(0, 8):
            s = (8 - rows_of_queens[i] + 1) + i
            queens_count_in_sec_diag[s] += 1
            queen_indexes[s].append(i)

        for i in range(0, 14):
            if queens_count_in_sec_diag[i] > 1:
                conflicts_count += queens_count_in_sec_diag[i]*(queens_count_in_sec_diag[i] - 1) / 2
                for index in queen_indexes[i]:
                    conflicting_queens.add(index)

        self.conflicting_queens = conflicting_queens
        self.conflicts_count = conflicts_count
#
# def has_conflicts(self):
#     for row in self._config:
#         if sum(row) > 1:
#             return True
#
#     for col in zip(*self._config):
#         if sum(col) > 1:
#             return True
#
#     # Sum diagonal left
#
#     # Sum diagonal right
#
#     return False
