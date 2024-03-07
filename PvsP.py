from board import *
from connectFour import *

def gamePvsP(board,start_p, sec_p):
    while True:        
        print(board)
        # #checks if there is winner
        # win = winner(board)
        # if not isinstance(win, bool):
        #     print(board)
        #     if win == 'Tie':
        #         print('Empate')
        #     else:
        #         print('Winner is ' + win)
        #     return win

        print("First Player")
        #gamePerson(board, start_p)
        turn, col, line = askForNextMove(board, start_p)
        move(board, turn, col, line)

        #checks if there is winner
        win = winner2(board, line, col, start_p)
        if win == True:
            print(board)
            if win == 'Tie':
                print('Empate')
            else:
                print('Winner is ' + start_p)
            return False
        
        print(board)

        # #checks if there is winner
        # win = winner(board)
        # if not isinstance(win, bool):
        #     if win == 'Tie': 
        #         print(win)
        #     print(board)
        #     print('Winner is ' + win)
        #     return win

        
        print("Second Player")
        #gamePerson(board, sec_p)
        turn, col, line = askForNextMove(board, sec_p)
        move(board, turn, col, line)

        #checks if there is winner
        win = winner2(board, line, col, sec_p)
        if not isinstance(win, bool):
            print(board)
            if win == 'Tie':
                print('Empate')
            else:
                print('Winner is ' + win)
            return win
