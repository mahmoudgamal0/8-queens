from Board import Board


def get_initial_configurations():
    board = Board()

    file = open("queens.txt", 'r')
    contents = file.read()
    file.close()

    board.config = contents
    return board


def write_new_configuration(config, name):
    writable_str = ''
    for row in config:
        writable_row = ['Q' if elem else '#' for elem in row]
        writable_str += ''.join(writable_row) + '\n'

    file = open(f"queens_out_{name}.txt", 'w')
    file.write(writable_str)
    file.close()
