from min import bestMove
import time
from board import Board
from astar import Astar
from connectFour import winnerAi
from monteCarlo import MCTS, Node
from randomGame import randomGame

def test_game(board: Board):
    c1 = 0
    csqrt2 = 0
    for i in range(10):
        print(i+1)
        board.resetBoard()
        m1 = MCTS(Node(board))
        m2 = MCTS2(Node2(board))
        order = ['X', 'O']
        playing = True
        while playing:
            
            board = m1.search(10).state
            m2.update_state(board)
            
            #checks winner
            winner = board.finished()
            if isinstance(winner, str):
                if winner == 'X': c1 += 1
                elif winner == 'O': csqrt2 += 1
                print('winner')
                break
            
            board = m2.search(10).state
            m1.update_state(board)
            
            #checks winner
            winner = board.finished()
            if isinstance(winner, str):
                if winner == 'X': c1 += 1
                elif winner == 'O': csqrt2 += 1
                print('winner')
                break
    print('c1: ' + str(c1))
    print('csqrt2: ' + str(csqrt2))
                
        