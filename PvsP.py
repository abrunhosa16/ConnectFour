from board import *
from connectFour import *

def winnerPvsP(board: Board, line:int, col:int) -> bool:
    win = board.finished_from(line, col)
    if isinstance(win, str):
        if win == 'Tie':
            print('Empate')
        else:
            print('O vencedor é ' + win + '.')
        return True
    return False

def gamePvsP(board, order):
    print(board)
    while True:   
        print('Primeiro jogador.')     
        line, col = askForNextMove(board, board.player)
        print(board)
        
        #checks winner
        if winnerPvsP(board, line, col):
            return None
        
        print("Segundo Jogador.")
        line, col = askForNextMove(board, board.player)
        print(board)
        
        #checks winner
        if winnerPvsP(board, line, col):
            return None
