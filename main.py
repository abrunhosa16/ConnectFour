from board import Board
from connectFour import askForFirstPlayer, askForAlgorithm, playAgain
from PvsP import gamePvsP
from astar import gameAstar
from min import gameMiniMax
from monteCarlo import gameMonteCarlo

def main():
    play = True
    order = askForFirstPlayer()
    board = Board(order[0])
    while play:
        board.resetBoard()
        game = askForAlgorithm()
        if game == 1:
            print("Escolhido Player vs Player.", end="\n")
            gamePvsP(board)
        if game == 2:
            print("Escolhido A*.", end="\n")
            gameAstar(board, order)
        if game == 3:
            print("Escolhido MonteCarlo", end="\n")
            gameMonteCarlo(board, order)
        if game == 4:
            print("Escolhido Minimax", end='\n')
            gameMiniMax(board, order)

        play = playAgain()


if __name__ == '__main__':
    main()