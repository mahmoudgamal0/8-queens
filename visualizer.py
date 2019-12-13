def visualize_board(board):
    for row in board:
        for col in row:
            val = 'Q' if col else '#'
            print(val, end='')
        print('\n')
    print('-------------------------')


def visualize(paths):
    print('===============================')
    for board in paths:
        visualize_board(board)
    print('===============================')