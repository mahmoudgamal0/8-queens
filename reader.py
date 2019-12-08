from Board import Board


def get_initial_configurations():
    board = Board()

    file = open("queens.txt", 'r')
    contents = file.read()
    file.close()

    board.config = contents
    return board
