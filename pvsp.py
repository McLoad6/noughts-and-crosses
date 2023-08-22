import numpy as np

def line_check(xoro, board):

    for x, row in enumerate(board):
        if ''.join(row).count(xoro * 5) > 0:
            win_line = []
            for y in range(len(row)):
                if board[x, y] == xoro:
                    win_line.append([x,y])
                    if len(win_line) == 5:
                        return win_line
                else:
                    win_line = []

    for y, col in enumerate(board.T):
        if ''.join(col).count(xoro * 5) > 0:
            win_line = []
            for x in range(len(row)):
                if board[x, y] == xoro:
                    win_line.append([x,y])
                    if len(win_line) == 5:
                        return win_line
                else:
                    win_line = []

    diagonals = []
    for i in range(-board.shape[0] + 1, board.shape[1]):
        diagonal = board[::-1, :].diagonal(i)
        diagonals.append(diagonal)

    after_middle = 0
    for diagonal in diagonals:
        if len(diagonal) == board.shape[0]:
            after_middle = 1
        if ''.join(diagonal).count(xoro * 5) > 0:
            win_line = []
            for row_idx, cell in enumerate(diagonal):
                if after_middle == 0:
                    if cell == xoro:
                        win_line.append([row_idx, len(diagonal) - row_idx - 1])
                        if len(win_line) == 5:
                            return win_line
                    else:
                        win_line = []
                else:
                    if cell == xoro:
                        win_line.append([row_idx + board.shape[0] - len(diagonal), board.shape[0] - row_idx - 1])
                        if len(win_line) == 5:
                            return win_line
                    else:
                        win_line = []

    diagonals2 = []
    for i in range(board.shape[1] - 1, -board.shape[0], -1):
        diagonal = board.diagonal(i)
        diagonals2.append(diagonal)
    
    after_middle = 0
    for diagonal in diagonals2:
        if len(diagonal) == board.shape[0]:
            after_middle = 1
        if ''.join(diagonal).count(xoro * 5) > 0:
            win_line = []
            for row_idx, cell in enumerate(diagonal):
                if after_middle == 0:
                    if cell == xoro:
                        win_line.append([board.shape[0] - len(diagonal) + row_idx, row_idx])
                        if len(win_line) == 5:
                            return win_line
                    else:
                        win_line = []
                else:
                    if cell == xoro:
                        win_line.append([row_idx, board.shape[0] - len(diagonal) + row_idx])
                        if len(win_line) == 5:
                            return win_line
                    else:
                        win_line = []

    return False

def winner(xoro, board, cell_size):
    if (win_line := line_check(xoro, board)) is not False:
        [y1, x1] = win_line[0]
        [y2, x2] = win_line[4]
        if x1 == x2:
            return [[x1 * cell_size + cell_size/2, y1 * cell_size + 10], [x2 * cell_size + cell_size/2, (y2 + 1) * cell_size - 10]]
        elif y1 == y2:
            return [[x1 * cell_size + 10, y1 * cell_size + cell_size/2], [(x2 + 1) * cell_size - 10, y2 * cell_size + cell_size/2]]
        elif (x1 - y1) == (x2 - y2):
            return [[y1 * cell_size + 10, x1 * cell_size + 10], [(y2 + 1) * cell_size - 10, (x2 + 1) * cell_size - 10]]
        else:
            return [[y1 * cell_size + 10, (x1+1) * cell_size - 10],[(y2+1) * cell_size - 10, x2 * cell_size + 10]]
    else:
        return False
    