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
<<<<<<< HEAD
        turn, col, line = askForNextMove(board, start_p)
        move(board, turn, col, line)
        print(possibleMoves(board))

=======
        gamePerson(board, start_p)
        
>>>>>>> 1f5e7db5765bbf963c2321cee26de85f182fe59c
        print(board)

        #checks if there is winner
        win = winner(board)
        if not isinstance(win, bool):
<<<<<<< HEAD
            if win == 'Tie':
                print('Empate')
            else:
                print('Winner is ' + win)
                return win
        
        print("Second Player")
        turn, col, line = askForNextMove(board, sec_p)
        move(board, turn, col, line)

        
       
=======
            if win == 'Tie': 
                print(win)
            print(board)
            print('Winner is ' + win)
            return win
        
        print("Second Player")
        gamePerson(board, sec_p)
>>>>>>> 1f5e7db5765bbf963c2321cee26de85f182fe59c
