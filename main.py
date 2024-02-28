from game.board import *
from game.connectFour import *
from algoritmos.PvsP import * 


def main():
    board = generateBoard()
    start_p = askForFirstPlayer()

    if start_p == 'w':
        sec_p = 'b'
    else:
        sec_p = 'w'

    game = int(input("Qual algoritmo queres? 1 - P vs P, 2 - A*, 3 - MC : "))
    if game == 1:
        print(" Escolhido Player vs Player", end="\n")
        gamePvsP(board, start_p, sec_p)


if __name__ == '__main__':
    main()
