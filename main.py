import copy
import time

from CSP import CSP
from GA import Genetic
from HillClimb import HillClimb
from fileIO import get_initial_configurations, write_new_configuration


def main():
    board = get_initial_configurations()

    # Hill Climbing
    time_hill = time.time()
    board_hill, explored_nodes_hill, path_hill = copy.deepcopy(board).solve(HillClimb())
    time_hill = time.time() - time_hill
    print_result('HillClimb', explored_nodes_hill, board_hill, time_hill)

    # CSP WITHOUT BACKTRACKING
    time_csp = time.time()
    board_csp, expanded_nodes_csp = copy.deepcopy(board).solve(CSP())
    time_csp = time.time() - time_csp
    print_result('CSP', expanded_nodes_csp, board_csp, time_csp)

    # GA
    time_ga = time.time()
    board_ga, expanded_nodes_ga = copy.deepcopy(board).solve(Genetic(100))
    time_ga = time.time() - time_ga
    print_result('GA', expanded_nodes_ga, board_ga, time_ga)


def print_result(method, expanded_nodes, board, exec_time):
    print(f"{method}: explored nodes count = {expanded_nodes}, cost = {board.cost}, time = {exec_time} secs")
    write_new_configuration(board.config, method)


if __name__ == '__main__':
    main()
