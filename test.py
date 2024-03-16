from min import bestMove
from astar import Astar
import time
from board import Board
from connectFour import winnerAi

def test_game(board: Board):
    print(board)
    order = ['X', 'O']
    while True:
        print('Minimax.')
        (line, col), *_ = bestMove(board, 8, float('-inf'), float('inf'), True, order)
        board.setPos(line, col, order[0])
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        board, line, col = Astar(board, order[1])
        print('A*')
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
test_game(Board('X'))