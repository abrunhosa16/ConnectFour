from game.connectFour import *
from game.board import *

def getLinePoints(line, player) -> int:
    if (line.count('X') != 0 and line.count('O') != 0): return 0
    if (line.count('X') == 3 and line.count('O') == 0): return 50
    if (line.count('X') == 2 and line.count('O') == 0): return 10
    if (line.count('X') == 1 and line.count('O') == 0): return 1
    if (line.count('X') == 0 and line.count('O') == 3): return -50
    if (line.count('X') == 0 and line.count('O') == 2): return -10
    if (line.count('X') == 0 and line.count('O') == 1): return -1
    return 0

def getPoints(board, player):
    win = winner(board)
    if win == 'X': return 512
    if win == 'O': return -512

    points = 0

    #horizontal
    for row in range(6):
        for col in range(4):
            points += getLinePoints( [board.getPos(row, col + i) for i in range(4)], player )

    #vertical
    for col in range(7):
        for row in range(3):
            points += getLinePoints( [board.getPos(row + i, col) for i in range(4)], player )

    #diagonal e-d c-b
    for row in range(3):
        for col in range(4):
            points += getLinePoints( [board.getPos(row + i, col + i) for i in range(4)], player )

    #diagonal e-d b-c
    for row in range(3,6,1):
        for col in range(4):
            points += getLinePoints( [board.getPos(row - i, col + i) for i in range(4)], player )

    return points

#penso que tenhamos de fazer algo como o algoritmo de djisktra ou assim pelo que vi
#não sei se devemos usar o conjunto g com os estados e respetivos pontos ou se com os movimtnos possiveis
def Astar(node, final):
    possibleMoves = availableMove(node)
    visited = []
    g = [(node, getPoints(node))]
    while g:
        cur = g[0]
