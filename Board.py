import copy
import random


class Board:
    def __init__(self):
        self._config = []
        self._conflicting_queens = {}
        self._conflicts_count = 0
        self._rows = []
        self._cost = 0
        self._explored_costs = {}

    @property
    def config(self):
        return self._config

    @property
    def conflicts_count(self):
        return self._conflicts_count

    @property
    def conflicting_queens(self):
        return self._conflicting_queens

    @property
    def cost(self):
        return self._cost

    @config.setter
    def config(self, value):
        board_list = value.split('\n')
        board_list = [elem.split(' ') for elem in board_list]
        self._config = []
        for line in board_list:
            self._config.append([(1 if elem == 'Q' else 0) for elem in line[0]])

        self.arrange_queens()

        rows_of_queens = []
        for j in range(0, 8):
            rows_of_queens.append(([i for i in range(0, 8) if self.config[i][j] == 1])[0])
        self._rows = rows_of_queens
        self.set_conflicting_pairs()

    def solve(self, algorithm):
        return algorithm.solve(self)

    def set_conflicting_pairs(self):
        self._conflicts_count, self._conflicting_queens = self.get_conflicting_queens(self._rows)

    def get_conflicting_queens(self, rows_of_queens):
        conflicting_queens = set()
        conflicts_count = 0
        queens_count_in_row = [0 for i in range(0, 8)]
        queen_indexes = [[] for i in range(0, 8)]
        for i in range(0, 8):
            queens_count_in_row[rows_of_queens[i]] += 1
            queen_indexes[rows_of_queens[i]].append(i)
        for i in range(0, 8):
            if queens_count_in_row[i] > 1:
                conflicts_count += queens_count_in_row[i] * (queens_count_in_row[i] - 1) / 2
                for index in queen_indexes[i]:
                    conflicting_queens.add(index)
        queen_indexes = [[] for i in range(0, 15)]
        queens_count_in_main_diag = [0 for i in range(0, 15)]
        for i in range(0, 8):
            s = rows_of_queens[i] + i
            queens_count_in_main_diag[s] += 1
            queen_indexes[s].append(i)
        for i in range(0, 14):
            if queens_count_in_main_diag[i] > 1:
                conflicts_count += queens_count_in_main_diag[i] * (queens_count_in_main_diag[i] - 1) / 2
                for index in queen_indexes[i]:
                    conflicting_queens.add(index)
        queen_indexes = [[] for i in range(0, 15)]
        queens_count_in_sec_diag = [0 for i in range(0, 15)]
        for i in range(0, 8):
            s = (7 - rows_of_queens[i]) + i
            queens_count_in_sec_diag[s] += 1
            queen_indexes[s].append(i)
        for i in range(0, 14):
            if queens_count_in_sec_diag[i] > 1:
                conflicts_count += queens_count_in_sec_diag[i] * (queens_count_in_sec_diag[i] - 1) / 2
                for index in queen_indexes[i]:
                    conflicting_queens.add(index)
        return conflicts_count, conflicting_queens

    def get_best_position(self, queen):
        current = copy.deepcopy(self._rows)
        minimum = 99999
        best = 0
        passed = False
        explored = 0
        for i in range(0, 8):
            if i == queen:
                continue
            current[queen] = i
            if tuple(current) in self._explored_costs:
                continue

            explored += 1
            passed = True
            conflicts_count, _ = self.get_conflicting_queens(current)
            if conflicts_count == minimum:
                if random.uniform(0, 1) > 0.5:
                    minimum = conflicts_count
                    best = i
            elif conflicts_count < minimum:
                minimum = conflicts_count
                best = i
            self._explored_costs[tuple(current)] = conflicts_count
        return best, minimum, passed,explored

    def random_move(self):
        rand_queen = random.randrange(8)
        rand_row = random.randrange(8)
        self._config[self._rows[rand_queen]][rand_queen] = 0
        self._config[rand_row][rand_queen] = 1
        self._rows[rand_queen] = rand_row
        self.set_conflicting_pairs()
        self._cost += 1
        if tuple(self._rows) in self._explored_costs:
            return 0
        return 1

    def move_queen(self, queen, new_row):
        self._config[self._rows[queen]][queen] = 0
        self._config[new_row][queen] = 1
        self._rows[queen] = new_row
        self.set_conflicting_pairs()
        self._cost += 1

    def configure_with_queens(self, queens):
        self._config = []
        self._rows = copy.deepcopy(queens)
        for i in range(0, 8):
            row = [1 if queens[j] == i else 0 for j in range(0, 8)]
            self._config.append(row)
        self.set_conflicting_pairs()

    def arrange_queens(self):
        col_sums = [sum(x) for x in zip(*self._config)]
        zero_index = []
        for i in range(0, 8):
            if col_sums[i] == 0:
                zero_index.append(i)

        for j, col in enumerate(col_sums):
            if col <= 1:
                continue

            rows = []
            for l in range(0, 8):
                if self.config[l][j] == 1:
                    rows.append(l)

            for i in rows:
                if col_sums[j] == 1:
                    break

                k = min(zero_index, key=lambda x: abs(x-j))
                moved = True
                # Right
                if k > j:
                    # Direct Right
                    if sum(self.config[i][j+1:k+1]) == 0:
                        self.config[i][k] = 1
                        self.config[i][j] = 0
                    else:
                        pos = [i, j]
                        down = False
                        while pos[1] != k:

                            # Direct Right
                            if pos[1] + 1 < 8 and self.config[pos[0]][pos[1] + 1] == 0:
                                pos[1] += 1
                            # Diag Right Up
                            elif pos[0] - 1 >= 0 and pos[1] + 1 < 8 and self.config[pos[0] - 1][pos[1] + 1] == 0:
                                pos[0] -= 1
                                pos[1] += 1
                            # Diag Right down
                            elif pos[0] + 1 < 8 and pos[1] + 1 < 8 and self.config[pos[0] + 1][pos[1] + 1] == 0:
                                pos[0] += 1
                                pos[1] += 1
                            # Down
                            elif pos[0] + 1 < 8 and self.config[pos[0] + 1][pos[1]] == 0 and not down:
                                pos[0] += 1
                            # UP
                            elif pos[0] - 1 >= 0 and self.config[pos[0] - 1][pos[1]] == 0:
                                down = True
                                pos[0] -= 1
                            else:
                                moved = False
                                break

                        self.config[i][j] = 0
                        self.config[pos[0]][pos[1]] = 1

                # Left
                else:
                    # Direct Left
                    if sum(self.config[i][k:j - 1]) == 0:
                        self.config[i][k] = 1
                        self.config[i][j] = 0
                    else:
                        pos = [i, j]
                        down = False
                        while pos[1] != k:

                            # Direct Left
                            if pos[1] - 1 >= 0 and self.config[pos[0]][pos[1] - 1] == 0:
                                pos[1] -= 1
                            # Diag Left Up
                            elif pos[0] - 1 >= 0 and pos[1] - 1 >= 0 and self.config[pos[0] - 1][pos[1] - 1] == 0:
                                pos[0] -= 1
                                pos[1] -= 1
                            # Diag Left down
                            elif pos[0] + 1 < 8 and pos[1] - 1 >= 0 and self.config[pos[0] + 1][pos[1] - 1] == 0:
                                pos[0] += 1
                                pos[1] -= 1
                            # Down
                            elif pos[0] + 1 < 8 and self.config[pos[0] + 1][pos[1]] == 0 and not down:
                                pos[0] += 1
                            # UP
                            elif pos[0] - 1 >= 0 and self.config[pos[0] - 1][pos[1]] == 0:
                                down = True
                                pos[0] -= 1
                            else:
                                moved = False
                                break

                        self.config[i][j] = 0
                        self.config[pos[0]][pos[1]] = 1

                if moved:
                    col_sums[j] -= 1
                    zero_index.remove(k)
