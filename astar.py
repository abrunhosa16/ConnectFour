from connectFour import *
from board import *

def getLinePoints(line) -> int:
    if (line.count('X') != 0 and line.count('O') != 0): return 0
    if (line.count('X') == 3 and line.count('O') == 0): return 50
    if (line.count('X') == 2 and line.count('O') == 0): return 10
    if (line.count('X') == 1 and line.count('O') == 0): return 1
    if (line.count('X') == 0 and line.count('O') == 3): return -50
    if (line.count('X') == 0 and line.count('O') == 2): return -10
    if (line.count('X') == 0 and line.count('O') == 1): return -1
    return 0

def getPoints(board):
    win = winner(board)
    if win == 'X': return 512
    if win == 'O': return -512

    points = 0

    #horizontal
    for row in range(6):
        for col in range(4):
            points += getLinePoints( [board.getPos(row, col + i) for i in range(4)])

    #vertical
    for col in range(7):
        for row in range(3):
            points += getLinePoints( [board.getPos(row + i, col) for i in range(4)])

    #diagonal e-d c-b
    for row in range(3):
        for col in range(4):
            points += getLinePoints( [board.getPos(row + i, col + i) for i in range(4)])

    #diagonal e-d b-c
    for row in range(3,6,1):
        for col in range(4):
            points += getLinePoints( [board.getPos(row - i, col + i) for i in range(4)])

    return points

#???
#falta colocar a logica de poder escolher qual a peça quero ser
def Astar(node : Board, turn):
    moves = possibleMoves(node)
    points = getPoints(node)
    best_move = [node, points]
    for move in moves:
        copy = node.boardCopy()
        copy.setPos(move[0], move[1], turn)
        copy_points = getPoints(copy)

        if turn == 'X':
            if copy_points == 512:
                return[copy, copy_points]
            if copy_points > best_move[1]:
                best_move = [copy, copy_points]
        else:
            if copy_points == -512:
                return[copy, copy_points]
            if copy_points < best_move[1]:
                best_move = [copy, copy_points]

    return best_move

tab1= Board()
tab1.setPos(5,0,'X')
tab1.setPos(5,1,'X')
tab1.setPos(5,2,'X')
tab1.setPos(5,5,'O')
tab1.setPos(4,5,'O')
new = Astar(tab1, 'O')
print(new[0], new[1])
