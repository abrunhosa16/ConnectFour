from game.board import *
from game.connectFour import *

def gamePvsP(board,start_p, sec_p):
    valid = True

    while valid or len(availableMove) > 0:
        print(board)
        win = winner(board)
        if not isinstance(win, bool):
            print('Winner is ' + win)
            return win

        print("First Player")
        turn, col, line = askForNextMove(board, start_p)
        move(board, turn, col, line)

        print(board)
        win = winner(board)
        if not isinstance(win, bool):

            if win == 'Tie': 
                print(win)

            print('Winner is ' + win)
            return win
        
        print("Second Player")
        turn, col, line = askForNextMove(board, sec_p)
        move(board, turn, col, line)