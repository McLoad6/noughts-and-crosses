import numpy as np

board = np.array([
    ['2', '2', '2', ' ', ' ', ' ', '1', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', ' ', '1', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', '1', '1', '2', '2', '2', ' '],
    [' ', ' ', '1', '1', ' ', '1', '1', ' ', ' ', ' '],
    [' ', ' ', ' ', '1', ' ', '1', '1', ' ', ' ', ' '],
    [' ', ' ', '1', ' ', ' ', ' ', '1', '1', '1', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
    [' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' '],
    ['2', ' ', ' ', '1', ' ', '1', ' ', ' ', ' ', ' ']
])

board2 = np.array([
    ['2', '2', ' ', ' ', ' ', ' ', '1'],
    [' ', ' ', ' ', '1', ' ', '1', ' '],
    ['2', ' ', ' ', ' ', ' ', ' ', ' '],
    ['2', ' ', ' ', ' ', ' ', ' ', '2'],
    [' ', '2', '2', ' ', ' ', ' ', '1'],
    [' ', ' ', ' ', '1', ' ', '1', ' '],
    [' ', ' ', '1', ' ', ' ', ' ', '1']
])

def get_crossing_lines(array, row, col):
    diagona1 = np.diagonal(array, col - row)
    diagonal2 = np.diagonal(np.fliplr(array), array.shape[1] - col - 1 - row)
    crossing_row = array[row]
    crossing_col = [x[col] for x in array]
    return diagona1, diagonal2, crossing_row, crossing_col

def get_all_lines(array):
    rows = array.tolist()
    columns = array.transpose().tolist()
    
    diags1 = [array.diagonal(i) for i in range(-array.shape[0] + 1, array.shape[1])]
    diagonals1 = [n.tolist() for n in diags1]

    diags2 = [np.fliplr(array).diagonal(i) for i in range(-array.shape[0] + 1, array.shape[1])]
    diagonals2 = [n.tolist() for n in diags2]
    return rows + columns + diagonals1 + diagonals2

def get_indexes_for_all_lines(array):
    rows_indexes = [[[j,i] for j in range(array.shape[1])] for i in range(array.shape[0])]
    column_indexes = [[[i,j] for j in range(array.shape[0])] for i in range(array.shape[1])]

    diags1 = [array.diagonal(i) for i in range(-array.shape[0] + 1, array.shape[1])]
    diagonals1 = [n.tolist() for n in diags1]
    after_middle = False
    diagonal_indexes1 = []
    for diagonal in diagonals1:
        diag_index = []
        if len(diagonal) == array.shape[0]:
            after_middle = True
        for row_idx in range(len(diagonal)):
            if after_middle:
                diag_index.append([row_idx + array.shape[0] - len(diagonal), row_idx])
            else:
                diag_index.append([row_idx, array.shape[0] - len(diagonal) + row_idx])
        diagonal_indexes1.append(diag_index)
    
    diags2 = [np.fliplr(array).diagonal(i) for i in range(-array.shape[0] + 1, array.shape[1])]
    diagonals2 = [n.tolist() for n in diags2]
    diagonal_indexes2 = []
    after_middle = False
    for diagonal in diagonals2:
        diag_index = []
        if len(diagonal) == array.shape[1]:
            after_middle = True
        for row_idx in range(len(diagonal)):
            if after_middle:
                diag_index.append([len(diagonal) - row_idx -1, row_idx])
            else:
                diag_index.append([array.shape[1] - row_idx -1, array.shape[1] - len(diagonal) + row_idx])
        diagonal_indexes2.append(diag_index)
    return rows_indexes + column_indexes + diagonal_indexes1 + diagonal_indexes2

def test_five(five:list):
    O = ''.join(five).count('2')
    X = ''.join(five).count('1')
    if O > 2 or X > 2:
        if O > X and O + X != 5 :
            if O == 4:
                index = [i for i in range(len(five)) if five[i] != '2']
                return [4,'2',index[0]]
            elif O == 3 and X == 0:
                if ''.join(five[:4]).count('2') == 3 or ''.join(five[-4:]).count('2') == 3:
                    if ''.join(five).count('2' * 3) == 1:
                        if five[1] != '2':
                            return [2,'2',1]
                        elif five[3] != '2':
                            return [2, '2', 3]
                        else:
                            return [3, '2', 0, 4]
                    else:
                        if five[1] != '2':
                            return [3, '2', 1, 4]
                        elif five[3] != '2':
                            return [3, '2', 3, 0]
                        elif five[0] != '2':
                            return [3, '2', 2, 0]
                        elif five[4] != '2':
                            return [3, '2', 2, 4]
        elif O < X and O + X != 5 :
            if X == 4:
                index = [i for i in range(len(five)) if five[i] != '1']
                return [4,'1',index[0]]
            elif X == 3 and O == 0:
                if ''.join(five[:4]).count('1') == 3 or ''.join(five[-4:]).count('1') == 3:
                    if ''.join(five).count('1' * 3) == 1:
                        if five[1] != '1':
                            return [2,'1',1]
                        elif five[3] != '1':
                            return [2, '1', 3]
                        else:
                            return [3, '1', 0, 4]
                    else:
                        if five[1] != '1':
                            return [3, '1', 1, 4]
                        elif five[3] != '1':
                            return [3, '1', 3, 0]
                        elif five[0] != '1':
                            return [3, '1', 2, 0]
                        elif five[4] != '1':
                            return [3, '1', 2, 4]

def test_a_line(line: list):
    possible_moves = []
    if len(line) >= 5:
        for i in range(len(line)-4):
            move = test_five(line[i:i+5])
            if move != None:
                if len(move) == 3:
                    move[2] = move[2] + i
                    possible_moves.append(move)
                elif len(move) == 4:
                    move[2] = move[2] + i
                    move[3] = move[3] + i
                    possible_moves.append(move)
    return possible_moves

def get_possible_moves(array):
    all_line_indexes = get_indexes_for_all_lines(array)
    possible_moves = []
    all_lines = get_all_lines(array)
    for i in range(len(all_lines)):
        moves = test_a_line(all_lines[i])
        if len(moves) != 0:
            for j in range(len(moves)):
                if len(moves[j]) == 3:
                    moves[j][2] = all_line_indexes[i][moves[j][2]]
                else:
                    moves[j][2] = all_line_indexes[i][moves[j][2]]
                    moves[j][3] = all_line_indexes[i][moves[j][3]]
            possible_moves.extend(moves)
    return possible_moves

def move_chooser(array, xoro):
    possible_moves = get_possible_moves(array)
    four_oponent = []
    three_my = []
    three_oponent = []
    two_my = []
    two_oponent = []
    for moves in possible_moves:
        if moves[1] == xoro:
            if moves[0] == 4:
                return moves[2] #four_my exit
            elif moves[0] == 3:
                three_my.append(moves[2:])
            else:
                two_my.append(moves[2:])
        else:
            if moves[0] == 4:
                four_oponent.append(moves[2:])
            elif moves[0] == 3:
                three_oponent.append(moves[2:])
            else:
                two_oponent.append(moves[2:])

    if len(four_oponent) == 1:
        return four_oponent[0][0]
    elif len(four_oponent) > 1:
        if len(three_my) >= 1:
            for i in three_my:
                if i[0] == four_oponent[0][0] or i[1] == four_oponent[0][0]:
                    return four_oponent[0][0]
        if len(three_oponent) >= 1:
            for i in three_oponent:
                if i[0] == four_oponent[0][0] or i[1] == four_oponent[0][0]:
                    return four_oponent[0][0]
        return four_oponent[0][0]
    if len(three_my) == 1:
        if len(three_oponent) >= 1:
            for i in three_oponent:
                if i[0] == three_my[0][0] or i[0] == three_my[0][1]:
                    return i[0]
                elif i[1] == three_my[0][0] or i[1] == three_my[0][1]:
                    return i[1]
        return three_my[0][0]   
       
    elif len(three_my) > 1:
        for i in three_my:
            for j in three_my:
                if i != j:
                    if i[0] == j[0] or i[0] == j[1]:
                        return i[0]
                    elif i[1] == j[0] or i[1] == j[1]:
                        return i[1]
        if len(three_oponent) >= 1:
            for i in three_my:
                for j in three_oponent:
                    if i[0] == j[0] or i[0] == j[1]:
                        return i[0]
                    elif i[1] == j[0] or i[1] == j[1]:
                        return i[1]
        
    if len(three_oponent) == 1:
        if len(two_my) >= 1:
            for i in two_my:
                if len(i) == 1:
                    if i[0] == three_oponent[0][0] or i[0] == three_oponent[0][1]:
                        return i[0]
                else:
                    if i[0] == three_oponent[0][0] or i[0] == three_oponent[0][1]:
                        return i[0]
                    elif i[1] == three_oponent[0][0] or i[1] == three_oponent[0][1]:
                        return i[1]
        if len(two_oponent) >= 1:
            for i in two_oponent:
                if len(i) == 1:
                    if i[0] == three_oponent[0][0] or i[0] == three_oponent[0][1]:
                        return i[0]
                else:
                    if i[0] == three_oponent[0][0] or i[0] == three_oponent[0][1]:
                        return i[0]
                    elif i[1] == three_oponent[0][0] or i[1] == three_oponent[0][1]:
                        return i[1]
        return three_oponent[0][0]
    elif len(three_oponent) > 1:
        for i in three_oponent:
            for j in three_oponent:
                if i != j:
                    if i[0] == j[0] or i[0] == j[1]:
                        return i[0]
                    elif i[1] == j[0] or i[1] == j[1]:
                        return i[1]
        if len(two_my) >=1:
            for i in two_my:
                for j in three_oponent:
                    if len(i) == 1:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                    else:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                        elif i[1] == j[0] or i[1] == j[1]:
                            return i[1]
        if len(two_oponent) >=1:
            for i in two_oponent:
                for j in three_oponent:
                    if len(i) == 1:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                    else:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                        elif i[1] == j[0] or i[1] == j[1]:
                            return i[1]
        return three_oponent[0][0]
    
    if len(two_my) == 1:
        if len(two_my[0]) == 2 and len(two_oponent) >= 1:
            for i in two_oponent:
                if len(i) == 1 and (i[0] == two_my[0][0] or i[0] == two_my[0][1]):
                    return i[0]
                elif len(i) == 2:
                    if i[0] == two_my[0][0] or i[0] == two_my[0][1]:
                        return i[0]
                    elif i[1] == two_my[0][0] or i[1] == two_my[0][1]:
                        return i[1]
        return two_my[0][0]
    elif len(two_my) > 1:
        for i in two_my:
            for j in two_my:
                if i != j:
                    if len(i) == 1 and len(j) == 1:
                        if i[0] == j[0]:
                            return i[0]
                    elif len(i) == 1 and len(j) == 2:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                    elif len(i) == 2 and len(j) == 1:
                        if i[0] == j[0] or i[1] == j[0]:
                            return j[0]
                    else:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                        elif i[1] == j[0] or i[1] == j[1]:
                            return i[1]
        if len(two_oponent) >=1:
            for i in two_my:
                for j in two_oponent:
                    if len(i) == 1 and len(j) == 1:
                        if i[0] == j[0]:
                            return i[0]
                    elif len(i) == 1 and len(j) == 2:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                    elif len(i) == 2 and len(j) == 1:
                        if i[0] == j[0] or i[1] == j[0]:
                            return j[0]
                    else:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                        elif i[1] == j[0] or i[1] == j[1]:
                            return i[1]
        return two_my[0][0]
    
    if len(two_oponent) == 1:
        return two_oponent[0][0]
    elif len(two_oponent) > 1:
        for i in two_oponent:
            for j in two_oponent:
                if i != j:
                    if len(i) == 1 and len(j) == 1:
                        if i[0] == j[0]:
                            return i[0]
                    elif len(i) == 1 and len(j) == 2:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                    elif len(i) == 2 and len(j) == 1:
                        if i[0] == j[0] or i[1] == j[0]:
                            return j[0]
                    else:
                        if i[0] == j[0] or i[0] == j[1]:
                            return i[0]
                        elif i[1] == j[0] or i[1] == j[1]:
                            return i[1]
        return two_oponent[0][0]
    return []

def next_step(array, xoro, opon):
    if (step := move_chooser(array,xoro)) != []:
        return step
    xoro_line2 = []
    xoro_line1 = []
    opon_line2 = []
    opon_line1 = []
    all_lines = get_all_lines(array)
    for i in range(len(all_lines)):
        xoro2 = ''.join(all_lines[i]).count(xoro * 2)
        xoro1 = ''.join(all_lines[i]).count(xoro)
        opon2 = ''.join(all_lines[i]).count(opon * 2)
        opon1 = ''.join(all_lines[i]).count(opon)
        if xoro2 > 0:
            xoro_line2.append(i)
        if xoro1 > 0:
            xoro_line1.append(i)
        if opon2 > 0:
            opon_line2.append(i)
        if opon1 > 0:
            opon_line1.append(i)
    for i in range(4,8):
        for j in range(4,8):
            if all_lines[j][i] == ' ':
                return [i,j]
    #if xoro_line2 != []:
        




#print(move_chooser(board2,'1'))