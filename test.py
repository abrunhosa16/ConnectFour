from min import bestMove
import time
from board import Board
from astar import Astar
from connectFour import winnerAi
from monteCarlo import MCTS, Node
from randomGame import randomGame

def test_game(board: Board):
    print(board)
    m =MCTS(board)
    order = ['X', 'O']
    while True:
        
        print('A*')
        board, *_ = Astar(board)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
        time.sleep(1)
        
        print('Random')
        randomGame(board)
        print(board)
        
        #checks winner
        if winnerAi(board, order):
            return None
        
