import random
from board import Board

def inputPlayer(letter:str) -> list:
    #retorna lista com a ordem do jogador
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def askForFirstPlayer() -> str:
    valid = False
    while not valid:
        piece = input("Queres ser X, O or R? ")
        if piece.upper() == "X" or piece.upper() == "O":
            return piece.upper()
        elif piece.upper() == "R":
            m = random.randint(0, 1)
            return "X" if m == 0 else "O"

def askForAlgorithm() -> int:
    while True:
        try:
            algorithm = int(input("Qual algoritmo queres? 1 - P vs P, 2 - A*, 3 - MC : "))
        except ValueError:
            print("Tente inteiros. \n")
            continue

        if algorithm in range(1, 4, 1):
            return algorithm
        else:
            print('Tente um número de 1 a 3. \n')
        
def playAgain() -> bool:
    while True:
        play = input(("Queres jogar de novo? S ou N. : "))
        if play.upper() == 'S':
            return True
        elif play.upper() == 'N':
            return False
        else:
            print('Tente S ou N. \n')

def testMove(board: Board, col) -> int:
    #-1 se não é possível
    for i in range(6):
        if board.getPos(5-i, col) == "-":
            return 5 - i
    return -1

def possibleMoves(board: Board, player:str) -> list:
    # retorna os proximos estados
    acc = []
    for col in range(7):
        line = testMove(board, col)
        if line != -1:
            cur = board.boardCopy()
            cur.setPos(line, col, player)
            acc.append((cur, line, col))
    return acc

def askForNextMove(board:Board, turn:str) -> tuple:
    while True:
        try:
            col = int(input("Em qual coluna? "))
        except ValueError:
            print("Tente inteiros.")
            continue
        
        if col > 6 or col < 0:
            print("Fora das margens.")
        else:
            line = testMove(board, col)
            
            if line == -1:
                print("Coluna cheia.")
            else:
                board.setPos(line, col, turn)
                return (line, col)

def winnerAi(board:Board, order:list) -> bool:
    win = board.finished()
    if isinstance(win, str):
        if win == 'Tie':
            print('Empate.')
        elif win == order[0]:
            print('Ganhaste.')
        else:
            print('A IA ganhou.')
        return True
    return False
