from board import Board
from connectFour import *
from PvsP import * 

board = Board()

def main():
    start_p = askForFirstPlayer()

    if start_p == 'X':
        sec_p = 'O'
    else:
        sec_p = 'X'

    game = int(input("Qual algoritmo queres? 1 - P vs P, 2 - A*, 3 - MC : "))
    if game == 1:
        print(" Escolhido Player vs Player", end="\n")
        gamePvsP(board, start_p, sec_p)


if __name__ == '__main__':
    main()
