import copy
import time

from CSP import CSP
from GA import Genetic
from fileIO import get_initial_configurations


def main():
    board = get_initial_configurations()


    # WITHOUT BACKTRACKING
    CSP_time = time.time()
    board1, expanded_nodes = copy.deepcopy(board).solve(CSP())
    CSP_time = time.time() - CSP_time
    print("explored nodes count = ", expanded_nodes, " cost = ", board1.cost, " time = ", CSP_time, " secs")

    GA_time = time.time()
    board2, expanded_nodes = copy.deepcopy(board).solve(Genetic(100))
    GA_time = time.time() - GA_time
    print("explored nodes count = ", expanded_nodes, " cost = ", board2.cost, " time = ", GA_time, " secs")



if __name__ == '__main__':
    main()
