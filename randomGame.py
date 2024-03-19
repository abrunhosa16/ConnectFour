from board import Board
from connectFour import possibleMoves
import random

def randomGame(board:Board):
    line, col = random.choice(possibleMoves(board))
    board.setPos(line, col)