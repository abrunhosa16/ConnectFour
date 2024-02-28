from board import *
from connectFour import *

def gamePvsP(board,start_p, sec_p):
    valid = True

    while valid:

        print(board)
        win = winner(board)
        if not isinstance(win, bool):
            print(board)
            print('Winner is ' + win)
            return win
        
        if len(possibleMoves(board)) == 0:
            print('Empate!!')
            break

        print("First Player")
        turn, col, line = askForNextMove(board, start_p)
        move(board, turn, col, line)
        
        print(board)
        win = winner(board)
        if not isinstance(win, bool):
            if win == 'Tie': 
                print(win)
            print(board)
            print('Winner is ' + win)
            return win
        
        if len(possibleMoves(board)) == 0:
            print('Empate!!')
            break
        
        print("Second Player")
        turn, col, line = askForNextMove(board, sec_p)
        move(board, turn, col, line)
        print(possibleMoves(board))

        
       