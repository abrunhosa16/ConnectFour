from board import *
from connectFour import *

def winnerPvsP(board:Board) -> bool:
    win = board.finished()
    if isinstance(win, str):
        if win == 'Tie':
            print('Empate')
        else:
            print('O vencedor é ' + win + '.')
        return True
    return False

def gamePvsP(board):
    print(board)
    while True:   
        print('Jogador ' + board.player + '.')     
        askForNextMove(board)
        print(board)
        
        if winnerPvsP(board):
            return 
    