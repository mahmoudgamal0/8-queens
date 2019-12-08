class Board:
    def __init__(self):
        self._config = []

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        board_list = value.split('\n')
        self._config = []

        for line in board_list:
            row = [1 if elem == 'Q' else 0 for elem in line]
            self._config.append(row)

    def solve(self, algorithm):
        algorithm.solve(self._config)

