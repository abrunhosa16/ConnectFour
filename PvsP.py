from board import *
from connectFour import *

def gamePvsP(board,start_p, sec_p):
    while True:
        print(board)

        #checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
            print(board)
            if win == 'Tie':
                print('Empate')
            else:
                print('Winner is ' + win)
            return win

        print("First Player")
        gamePerson(board, start_p)
        
        print(board)

        #checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
            if win == 'Tie': 
                print(win)
            print(board)
            print('Winner is ' + win)
            return win
        
        print("Second Player")
        gamePerson(board, sec_p)
