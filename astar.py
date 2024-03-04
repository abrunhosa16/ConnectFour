from connectFour import *
from board import *
import time

def getLinePoints(line, player) -> int:
    opponent = 'X' if player == 'O' else 'O'
    if (line.count('X') != 0 and line.count('O') != 0): return 0
    if (line.count('X') == 3 and line.count('O') == 0): 
        if 'X' == opponent: return 50
        else: return 50
    if (line.count('X') == 2 and line.count('O') == 0):
        if 'X' == opponent: return 10
        else: return 10
    if (line.count('X') == 1 and line.count('O') == 0): return 1
    if (line.count('X') == 0 and line.count('O') == 3):
        if 'O' == opponent: return -50
        else: return -50
    if (line.count('X') == 0 and line.count('O') == 2):
        if 'O' == opponent: return -10
        else: return -10
    if (line.count('X') == 0 and line.count('O') == 1): return -1
    return 0

def getPoints(board, player):
    win = winner(board)
    if win == 'X': return 512
    if win == 'O': return -512

    points = 16 if player == 'X' else -16

    #horizontal
    for row in range(6):
        for col in range(4):
            points += getLinePoints( [board.getPos(row, col + i) for i in range(4)], player)

    #vertical
    for col in range(7):
        for row in range(3):
            points += getLinePoints( [board.getPos(row + i, col) for i in range(4)], player)

    #diagonal e-d c-b
    for row in range(3):
        for col in range(4):
            points += getLinePoints( [board.getPos(row + i, col + i) for i in range(4)], player)

    #diagonal e-d b-c
    for row in range(3,6,1):
        for col in range(4):
            points += getLinePoints( [board.getPos(row - i, col + i) for i in range(4)], player)

    return points

def Astar(node : Board, ai):
    moves = possibleMoves(node)
    points = getPoints(node, ai)
    best_move = [node, points]
    for move in moves:
        copy = node.boardCopy()
        copy.setPos(move[0], move[1], ai)
        copy_points = getPoints(copy, ai)
        if ai == 'X':
            if copy_points == 512:
                return [copy, move[1]]
            if copy_points > best_move[1]:
                best_move = [copy, copy_points, move[1]]
        else:
            if copy_points == -512:
                return [copy, move[1]]
            if copy_points < best_move[1]:
                best_move = [copy, copy_points, move[1]]

    return [best_move[0], best_move[2]]

def gameAstar(board: Board, person):
    #gives a list [person, ai]
    order = inputPlayer(person)

    while True:
        print(board)

        #checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
            print('O vencedor é  ' + win + '.')
            return win
        
        print('Tua vez.')
        board, col = Astar(board, order[0])

        print(board)
        time.sleep(2)


        #checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
            if win == 'Tie': 
                print('Empate.')
            print('O vencedor é ' + win + '.')
            return win

        board, col = Astar(board, order[1])
        print('A AI pôs uma peça na coluna ' + str(col) + '.')

# b = Board()
# # b.setPos(5,0,'X')
# # b.setPos(4,0,'X')
# # b.setPos(3,0,'X')
# b.setPos(5,2,'O')
# b.setPos(5,3,'O')
# b.setPos(5,4,'O')
# print(b)
# print(getPoints(b))