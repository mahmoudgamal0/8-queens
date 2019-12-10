import copy
import time

from CSP import CSP
from fileIO import get_initial_configurations


def main():
    board = get_initial_configurations()


    # WITHOUT BACKTRACKING
    CSP_time = time.time()
    board1, expanded_nodes = copy.deepcopy(board).solve(CSP())
    CSP_time = time.time() - CSP_time
    print("explored nodes count = ", expanded_nodes, " cost = ", board1.cost, " time = ", CSP_time, " secs")



if __name__ == '__main__':
    main()
