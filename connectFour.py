import random
from board import Board

tabuleiro = Board()

def inputPlayer(letter) -> list:
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

def testMoveValidity(board: Board, col) -> int:
    #retorna -1 se não for valido
    #retorna o numero da coluna se for valido
    for i in range(6):
        if board.getPos(5-i, col) == "-":
            return 5 - i
    return -1

def testMove(board: Board, col) -> bool | int:

    if col > 6 or col < 0:
        print("Fora das margens")
        return False

    position = testMoveValidity(board, col)

    if position == -1:
        print("Coluna não disponível")
        return False

    return position

def move(board: Board, turn, col, line) -> None:
    board.setPos(line, col, turn)

def askForNextMove(board, turn) -> tuple:
    while True:
        try:
            move_col = int(input("Em qual coluna? "))
        except ValueError:
            print("Tente inteiros.")
            continue

        move = testMove(board, move_col)
        if isinstance(move, bool):
            print("A jogada não é válida. Tente novamente.")
        else:
            return (turn, move_col, move)

def winner(board: Board, row, col) -> str | bool:
    #verifica apenas as linhas que incluem a casa onde foi jogada uma peça
    if board.getRow(0).count('-') == 0:
        return 'Tie'
    
    #horizontal
    limits_col = [max(0, col-3), min(6, col+3)]
    sequence = [board.getPos(row, limits_col[0]), 0]
    for i in range(limits_col[0], limits_col[1] + 1, 1):
        if board.getPos(row, i) != sequence[0]:
            sequence = [board.getPos(row, i), 1]
        else:
            sequence[1] += 1
        if (sequence[1] == 4 and sequence[0] != '-'):
            return board.getPos(row, col)
        
    #vertical
    limits_row = [max(0, row-3), min(5, row+3)]
    sequence = [board.getPos(row, limits_row[0]), 0]
    for i in range(limits_row[0], limits_row[1] + 1, 1):
        if board.getPos(i, col) != sequence[0]:
            sequence = [board.getPos(i, col), 1]
        else:
            sequence[1] += 1
        if (sequence[1] == 4 and sequence[0] != '-'):
            return board.getPos(row, col)
        
    #vertical e-d c-b
    interval = min(limits_row[1] - limits_row[0], limits_col[1] - limits_col[0]) #numero de casas da diagonal a ver
    sequence = [board.getPos(limits_row[0], limits_col[0]), 0]
    for i in range(interval):
        if board.getPos(limits_row[0] + i, limits_col[0] + i) != sequence[0]:
            sequence = [board.getPos(limits_row[0] + i, limits_col[0] + i), 1]
        else:
            sequence[1] += 1
        if (sequence[1] == 4 and sequence[0] != '-'):
            return board.getPos(row, col)
        
    #vertical e-d b-c
    sequence = [board.getPos(limits_row[0], limits_col[0]), 0]
    for i in range(interval):
        if board.getPos(limits_row[1] - i, limits_col[0] + i) != sequence[0]:
            sequence = [board.getPos(limits_row[1] - i, limits_col[0] + i), 1]
        else:
            sequence[1] += 1
        if (sequence[1] == 4 and sequence[0] != '-'):
            return board.getPos(row, col)
    
    return False

def possibleMoves(board: Board) -> list:
    # retorna uma lista com movimentos possiveis para a IA
    acc = []
    for i in range(7):
        position = testMoveValidity(board, i)
        if position != -1:
            acc.append((position, i))
    return acc