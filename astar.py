from connectFour import *
from board import *
import time

def getLinePoints(line, player) -> int:
    opponent = 'X' if player == 'O' else 'O'
    if (line.count('X') != 0 and line.count('O') != 0): return 0
    
    if (line.count('X') == 3 and line.count('O') == 0): 
        if 'X' == opponent: return 250
        else: return 50
    if (line.count('X') == 2 and line.count('O') == 0): 
        if 'X' == opponent: return 50
        else: return 10
    if (line.count('X') == 1 and line.count('O') == 0): return 1
    
    if (line.count('X') == 0 and line.count('O') == 3):
        if 'O' == opponent: return -250
        else: return -50
    if (line.count('X') == 0 and line.count('O') == 2):
        if 'O' == opponent: return -50
        else: return -10
    if (line.count('X') == 0 and line.count('O') == 1): return -1
    
    return 0

def getPoints(board, player) -> int:
    win = winnerAllBoard(board)
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

def Astar(node : Board, ai) -> list:
    moves = possibleMoves(node)
    points = getPoints(node, ai)
    best_move = [node, points, 0]
    for move in moves:
        copy = node.boardCopy()
        copy.setPos(move[0], move[1], ai)
        copy_points = getPoints(copy, ai)
        if ai == 'X':
            if copy_points == 512:
                return [copy, move[0], move[1]]
            if copy_points > best_move[1]:
                best_move = [copy, copy_points, move[0], move[1]]
        else:
            if copy_points == -512:
                return [copy, move[0], move[1]]
            if copy_points < best_move[1]:
                best_move = [copy, copy_points, move[0], move[1]]
    
    #para verificar se ela não joga         
    if node == best_move[0]:
        print('-------------------------------------------------------------------------------------------')
        
    return [best_move[0], best_move[2], best_move[3]]

def gameAstar(board: Board, order):
    print(board)
    while True:
        print('Tua vez.')
        turn, col, line = askForNextMove(board, order[0])
        move(board, turn, col, line)
        print(board)
        
        #checks winner
        win = winner(board, line, col)
        if isinstance(win, str):
            if win == 'Tie':
                print('Empate.')
            elif win == order[0]:
                print('Ganhaste.')
            else:
                print('A IA ganhou.')
            return False
        
        board, line, col = Astar(board, order[1])
        print('A IA 2 pôs uma peça na coluna ' + str(col) + '.')
        print(board)
        
        #checks winner
        win = winner(board, line, col)
        if isinstance(win, str):
            if win == 'Tie':
                print('Empate')
            elif win == order[0]:
                print('Ganhaste.')
            else:
                print('A IA ganhou.')
            return False