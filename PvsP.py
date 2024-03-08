from board import *
from connectFour import *

def gamePvsP(board, order):
    start_p, sec_p = order
    print(board)
    while True:   
        print('Primeiro jogador.')     
        turn, col, line = askForNextMove(board, start_p)
        move(board, turn, col, line)
        print(board)
        
        #checks winner
        win = winner(board, line, col)
        if isinstance(win, str):
            if win == 'Tie':
                print('Empate')
            else:
                print('O vencedor é ' + win + '.')
            return False
        
        print("Segundo Jogador.")
        turn, col, line = askForNextMove(board, sec_p)
        move(board, turn, col, line)
        print(board)
        #checks winner
        win = winner(board, line, col)
        if isinstance(win, str):
            if win == 'Tie':
                print('Empate')
            else:
                print('O vencedor é ' + win + '.')
            return False
