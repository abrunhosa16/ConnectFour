from board import *
from connectFour import *
from astar import getPoints
import time 

def scoreLine(line:list , player:str, n) -> int:
    score = 0

    if line.count(player) == 4 and n == 4:
        score += 1

    if line.count(player) == 3 and line.count('-') == 1 and n == 3:
        score += 1

    if line.count(player) == 2 and line.count('-') == 2 and n == 2:
        score += 1

    return score  

def centrais(board:Board, player:str, n) -> int:
    points = 0
    for line in range(6):
        if board.getPos(line, 4) == player and n == 4:
            points += 1
        if board.getPos(line, 3) == player or board.getPos(line, 5) == player and n == 3:
            points += 1
    return points

# Function to calculate the overall score of the board
def score_position(board:Board , player:str, n) -> int:
    points = 0
    for line in range(6):
        for col in range(7):
            #horizontal
            if col < 4:
                points += scoreLine( [board.getPos(line, col+i) for i in range(4)], player, n)

            #vertical
            if line < 3:
                points += scoreLine( [board.getPos(line + i, col) for i in range(4)], player, n)
                
            #diagonal positiva
            if line < 3 and col < 4:
                points += scoreLine( [board.getPos(line + i, col + i) for i in range(4)], player, n)

            #diagonal negativa
            if line > 2 and col < 4:
                points += scoreLine( [board.getPos(line - i, col + i) for i in range(4)], player, n)
    return points

def heuristica(board, player):
    order = inputPlayer(player)
    central = 10 * (centrais(board, order[0], 4) - centrais(board, order[1], 4))
    neigh_center = 8 * centrais(board, order[0], 3) - centrais(board, order[1], 3)
    strong_line = 100 * (score_position(board, order[0], 4) - score_position(board, order[1], 4))
    line = 20 * score_position(board, order[0], 3) - 40 * score_position(board, order[1], 3)
    weak_line =  5 * score_position(board, order[0], 2) - score_position(board, order[1], 2)
    
    return  central + neigh_center + strong_line + line + weak_line
    

def bestMove(board:Board , depth:int , alpha, beta, maximizing:bool , order:list):
    possible_moves = possibleMoves(board)
    terminal_node = isinstance(board.finished(), str)

    if depth == 0 or terminal_node:
        return None, heuristica(board, order[1])

    if maximizing:
        max_value = float('-inf')
        best_move = None

        for line, col in possible_moves:
            copy = board.boardCopy()
            copy.setPos(line, col, order[1])
            _, new_score = bestMove(copy, depth - 1, alpha, beta, False, order)

            if new_score > max_value:
                max_value = new_score
                best_move = (line, col)
            alpha = max(alpha, max_value)

            if alpha >= beta:
                break
        return best_move, max_value
        
    else:
        min_value = float('inf')
        best_move = None

    for line, col in possible_moves:
        copy = board.boardCopy()
        copy.setPos(line, col, order[0])
        _, new_score = bestMove(copy, depth - 1, alpha, beta, True, order)
        if new_score < min_value:
            min_value = new_score
            best_move = (line, col)
        beta = min(beta, min_value)
        if alpha >= beta:
            break
    return best_move, min_value
    
    
def gameMiniMax(board: Board, order:list):
    print(board)
    while True:
        # print('Tua vez.')
        # line, col = askForNextMove(board, board.player)
        # print(board)

        (line, col), *_ = bestMove(board, 6, float('-inf'), float('inf'), False, order)
        board.setPos(line, col, board.player)
        print('A IA 1 pôs uma peça na coluna ' + str(col) + '.')
        print(board)
        
        #checks winner
        if winnerAi(board, order, (line, col)):
            return None
        
        (line, col), *_ = bestMove(board, 4, float('-inf'), float('inf'), True, order)
        board.setPos(line, col, board.player)
        print('A IA 2 pôs uma peça na coluna ' + str(col) + '.')
        print(board)
        
        #checks winner
        if winnerAi(board, order, (line, col)):
            return None
