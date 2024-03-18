from min import bestMove
import time
from board import Board
from connectFour import winnerAi
from monteCarlo import MCTS, Node

def test_game(board: Board):
    print(board)
    m =MCTS(board)
    order = ['X', 'O']
    while True:
        
        print('Minimax')
        (lin, col), *_ = bestMove(board, 6, float('-inf'), float('inf'), False, order)
        board.setPos(lin, col, board.player)
        m.root = Node(board)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        print('Monte Carlo')
        board = m.search(10).state
        m.update_state(board)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
test_game(Board('X'))