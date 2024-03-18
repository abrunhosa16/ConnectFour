from board import *
from connectFour import *
from astar import getPoints
import time 

def scoreLine(line:list , player:str) -> int:
    score = 0
    
    if line.count(player) == 4:
        score += 100
    if line.count(player) == 3 and line.count('-') == 1:
        score += 8
    if line.count(player) == 2 and line.count('-') == 2:
        score += 4
    
    if line.count(player) == 0 and line.count('-') == 0:
        score -= 100


    return score  

# Function to calculate the overall score of the board
def score_position(board:Board , player:str) -> int:
    points = 0
    for line in range(6):
        for col in range(7):
            #horizontal
            if col < 4:
                points += scoreLine( [board.getPos(line, col+i) for i in range(4)], player)

            #vertical
            if line < 3:
                points += scoreLine( [board.getPos(line + i, col) for i in range(4)], player)
                
            #diagonal positiva
            if line < 3 and col < 4:
                points += scoreLine( [board.getPos(line + i, col + i) for i in range(4)], player)

            #diagonal negativa
            if line > 2 and col < 4:
                points += scoreLine( [board.getPos(line - i, col + i) for i in range(4)], player)
    return points

def bestMove(board:Board , depth:int , alpha, beta, maximizing:bool , order:list):
    possible_moves = possibleMoves(board)
    terminal_node = isinstance(board.finished(), str)

    if depth == 0 or terminal_node:
        return None, score_position(board, order[1])

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
    
# def maxValue(board:Board , depth:int , alpha, beta, maximizing:bool , order:list, possible_moves):
#     max_value = float('-inf')
#     best_move = None

#     for line, col in possible_moves:
#         copy = board.boardCopy()
#         copy.setPos(line, col, order[1])
#         print(bestMove(copy, depth, alpha, beta, False, order))
#         _, new_score = bestMove(copy, depth - 1, alpha, beta, False, order)

#         if new_score > max_value:
#             max_value = new_score
#             best_move = (line, col)
#         alpha = max(alpha, max_value)

#         if alpha >= beta:
#             break
#     return best_move, max_value

# def minValue(board:Board , depth:int , alpha, beta, maximizing:bool , order:list, possible_moves):
#     min_value = float('inf')
#     best_move = None

#     for line, col in possible_moves:
#         copy = board.boardCopy()
#         copy.setPos(line, col, order[0])
#         _, new_score = bestMove(copy, depth - 1, alpha, beta, True, order)
#         if new_score < min_value:
#             min_value = new_score
#             best_move = (line, col)
#         beta = min(beta, min_value)
#         if alpha >= beta:
#             break
#     return best_move, min_value
    
def gameMiniMax(board: Board, order:list):
    print(board)
    while True:
        print('Tua vez.')
        line, col = askForNextMove(board, board.player)
        print(board)
        
        #checks winner
        if winnerAi(board, order, (line, col)):
            return None
        
        (line, col), *_ = bestMove(board, 5, float('-inf'), float('inf'), True, order)
        board.setPos(line, col, board.player)
        print('A IA pôs uma peça na coluna ' + str(col) + '.')
        print(board)
        
        #checks winner
        if winnerAi(board, order, (line, col)):
            return None
