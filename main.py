import copy
import time

from CSP import CSP
from GA import Genetic
from HillClimb import HillClimb
from K_beam import K_beam
from fileIO import get_initial_configurations, write_new_configuration
from gui import draw_grid
from visualizer import visualize


def main():
    board = get_initial_configurations()
    run_hill(board)
    run_csp(board)
    run_genetic(board)
    run_kbeam(board)


def run_hill(board):
    # Hill Climbing
    time_hill = time.time()
    board_hill, explored_nodes_hill, path_hill = copy.deepcopy(board).solve(HillClimb())
    time_hill = time.time() - time_hill
    print_result('HillClimb', explored_nodes_hill, board_hill, time_hill)
    visualize(path_hill)

    draw_grid(path_hill)


def run_csp(board):
    # CSP WITHOUT BACKTRACKING
    time_csp = time.time()
    board_csp, expanded_nodes_csp, path_csp = copy.deepcopy(board).solve(CSP())
    time_csp = time.time() - time_csp
    print_result('CSP', expanded_nodes_csp, board_csp, time_csp)
    visualize(path_csp)
    draw_grid(path_csp)


def run_kbeam(board):
    # K-beam
    k_beam = K_beam()
    best_time = 100
    best_time_pram = {}
    best_cost = 100
    best_cost_pram = {}
    found = False
    for k in range(1, 20):
        time_k = time.time()
        board_K_beam, expanded_nodes_k_beam, cost = k_beam.solve(board.config, k)
        time_k = time.time() - time_k
        if board_K_beam != None:
            found = True
            board_K_beam.cost = cost
            if best_time > time_k:
                best_time = time_k
                best_time_pram['k'] = k
                best_time_pram['name'] = str(k) + "-beam"
                best_time_pram['time'] = time_k
                best_time_pram['cost'] = cost
                best_time_pram['nodes'] = expanded_nodes_k_beam
                best_time_pram['board'] = board_K_beam
            if best_cost > cost:
                best_cost = cost
                best_cost_pram['k'] = k
                best_cost_pram['name'] = str(k) + "-beam"
                best_cost_pram['time'] = time_k
                best_cost_pram['cost'] = cost
                best_cost_pram['nodes'] = expanded_nodes_k_beam
                best_cost_pram['board'] = board_K_beam
    if (found):
        print_result(best_time_pram['name'], best_time_pram['nodes'],
                     best_time_pram['board'], best_time_pram['time'])
        print_result(best_cost_pram['name'], best_cost_pram['nodes'],
                     best_cost_pram['board'], best_cost_pram['time'])


def run_genetic(board):
    # GA
    time_ga = time.time()
    board_ga, expanded_nodes_ga = copy.deepcopy(board).solve(Genetic(100))
    time_ga = time.time() - time_ga
    print_result('GA', expanded_nodes_ga, board_ga, time_ga)


def print_result(method, expanded_nodes, board, exec_time):
    print(f"{method}: explored nodes count = {expanded_nodes}, cost = {board.cost}, time = {exec_time} secs")
    write_new_configuration(board.config, method)


# Run ALL
if __name__ == '__main__':
    main()


# Run Hill Only
if __name__ == '__main__':
    board = get_initial_configurations()
    run_hill(board)


# Run CSP Only
if __name__ == '__main__':
    board = get_initial_configurations()
    run_csp(board)

# Run KBeam Only
if __name__ == '__main__':
    board = get_initial_configurations()
    run_kbeam(board)


# Run Genetic Only
if __name__ == '__main__':
    board = get_initial_configurations()
    run_genetic(board)
