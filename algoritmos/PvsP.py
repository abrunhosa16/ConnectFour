from game.board import *
from game.connectFour import *

def gamePvsP(board,start_p, sec_p):
    valid = True

    while valid or len(availableMoveAi) > 0:
        printBoard(board)
        win = winner(board)
        if not isinstance(win, bool):
            print('Winner is ' + win)
            return win

        print("First Player")
        turn, col, line = askForNextMove(board, start_p)
        move(board, turn, col, line)


        win = winner(board)
        if not isinstance(win, bool):
            print('Winner is ' + win)
            return win
        
        printBoard(board)
        print("Second Player")
        turn, col, line = askForNextMove(board, sec_p)
        move(board, turn, col, line)