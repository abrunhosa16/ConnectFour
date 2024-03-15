from board import *
from connectFour import *

ROWS = 6
COLS = 7

def scoreLine(line, player) -> int:
    opponent ='O' if player =='X' else 'X'
    score = 0
    if line.count(player) == 4:
        score +=100
    if line.count(player) == 3 and line.count('-') == 1:
        score += 8
    if line.count(player) == 2 and line.count('-') == 2:
        score += 4
    
    if line.count(opponent) == 3 and line.count('-') == 1:
        score -= 8
    if line.count(opponent) == 2 and line.count('-') == 2:
        score -= 4

    return score  


# Function to calculate the overall score of the board
def score_position(board, player):
    points = 0
    
#horizontal ALL POSSIBLE LINES CHECKED
    for row in range(6):
        for col in range(4):
            points += scoreLine( [board.getPos(row, col + i) for i in range(4)], player)

    #vertical ALL POSSIBLE LINES CHECKED
    for col in range(7):
        for row in range(3):
            points += scoreLine( [board.getPos(row + i, col) for i in range(4)], player)

    #diagonal e-d c-b ALL POSSIBLE LINES CHECKED
    for row in range(3):
        for col in range(4):
            points += scoreLine( [board.getPos(row + i, col + i) for i in range(4)], player)

    #diagonal e-d b-c ALL POSSIBLE LINES CHECKED
    for row in range(3,6,1):
        for col in range(4):
            points += scoreLine( [board.getPos(row - i, col + i) for i in range(4)], player)

    return points




def bestMove(board, depth, alpha, beta, max_player):
    possMoves = possibleMoves(board)
    win = winner(board) == 'Tie'
    

    terminal_node =  win or winner(board)
    player1, player2 = inputPlayer(max_player)

    if depth== 0 or terminal_node:
        if terminal_node:
            if terminal_node == player2:
                return (None, 10000000)
            if terminal_node == player1:
                return (None, -10000000)
            else: # no more valid moves
                return (None, 0)
        else:
            return (None, score_position(board, player2))
    if max_player:
        value = -float('inf')
        best_col = possMoves[0][1]

        for col in possMoves:
            copy = board.boardCopy()
            move(copy, player2, col[1], col[0])
            new_score = bestMove(copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col[1]
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = float('inf')
        best_col = possMoves[0][1]

        for col in possMoves:
            copy = board.boardCopy()
            move(copy, player1, col[1], col[0])
            new_score = bestMove(copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col[1]
            beta = min(beta, value)
            if alpha >= beta:
                break 
        return best_col, value 

import time 

def gameMiniMax(board: Board, person):
    #gives a list [person, ai]
    order = inputPlayer(person)

    while True:
        print(board)

        # checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
            print('O vencedor é  ' + win + '.')
            return win
        
        print('Tua vez.')
        turn, col, line = askForNextMove(board, order[0])
        move(board, turn, col, line)
    
        print('A AI 1 pôs uma peça na coluna ' + str(col) + '.')

        print(board)


        #checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
            if win == 'Tie': 
                print('Empate.')
            print('O vencedor é ' + win + '.')
            return win
        
        minMaxMove, value = bestMove(board, 4, -float('inf'), float('inf'), True)
        print(minMaxMove)
        move(board, order[1], minMaxMove, testMoveValidity(board, minMaxMove))
        

        
        print('A AI 2 pôs uma peça na coluna ' + str(col) + '.')
