from board import Board
from connectFour import possibleMoves
import random

def randomGame(board:Board):
    line, col = random.choce(possibleMoves(board))
    board.setPos(line, col, board.player)