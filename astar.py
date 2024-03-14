from connectFour import *
from board import *

def getLinePoints(line:int, player:str) -> int:
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

def getPoints(board:Board, player: str) -> int:
    win = board.finished()
    if win == 'X': return 512
    if win == 'O': return -512
    if win == 'Tie': return 0

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

def Astar(node:Board, ai:str) -> list:
    moves = possibleMoves(node, ai)
    points = getPoints(node, ai)
    best_move = [node, points, 0]
    for move in moves:
        state, line, col = move
        state_points = getPoints(state, ai)
        if ai == 'X':
            if state_points == 512:
                return state
            if state_points > best_move[1]:
                best_move = [state, state_points, line, col]
        else:
            if state_points == -512:
                return [state, line, col]
            if state_points < best_move[1]:
                best_move = [state, state_points, line, col]
    
    #para verificar se ela não joga         
    if node == best_move[0]:
        print('-------------------------------------------------------------------------------------------')
        
    return [best_move[0], best_move[2], best_move[3]]

def gameAstar(board:Board, order:list):
    print(board)
    while True:
        print('Tua vez.')
        askForNextMove(board, order[0])
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        board, line, col = Astar(board, order[1])
        print('A IA 2 pôs uma peça na coluna ' + str(col) + '.')
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None