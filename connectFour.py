import random
from board import Board

tabuleiro = Board()

def inputPlayer(letter):
    # define qual letra para cada jogador retorna [X, O] or [O, X]
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def askForFirstPlayer():
    #perguntar ao jogador quem é que deve jogar primeiro, as opções
    #podem ser por exemplo "white", "black" ou "random" e retorna o valor relacionado
    valid = False
    while not valid:
        piece = input("Queres ser X, O or R? ")
        if piece.upper() == "X" or piece.upper() == "O":
            return piece.upper()
        elif piece.upper() == "R":
            m = random.randint(0, 1)
            return "X" if m == 0 else "O"

def testMoveValidity(board: Board, col) -> int | bool:
    # testa se a jogada é válida se a casa esta vazia e qual a posição esta vazia
    # retorna a posição que esta vazia ou false
    for i in range(6):
        if board.getPos(5-i, col) == "-":
            return 5 - i
    return False

def testMove(board: Board, col) -> bool | int:

    if col > 6 or col < 0:
        print("Fora das margens")
        return False

    position = testMoveValidity(board, col)

    if not isinstance(position, int):
        print("Coluna não disponível")
        return False

    return position

def move(board: Board, turn, col, line) -> None:
    board.setPos(line, col, turn)

def askForNextMove(board, turn):
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

def winner(board: Board):

    for row in range(6):

        #empate
        if (row == 0):
            line = board.getRow(row)
            if (line == ['w'] * 7 or line == ['b'] * 7): return 'Tie'

        for col in range(7):
            
            #horizontal
            if col <= 3:
                if (board.getPos(row, col) == board.getPos(row, col + 1) == board.getPos(row, col + 2) == board.getPos(row, col + 3) and board.getPos(row, col) != '-'):
                    return board.getPos(row, col)

            #vertical
            if row <= 2:
                if (board.getPos(row, col) == board.getPos(row + 1, col) == board.getPos(row + 2, col) == board.getPos(row + 3, col) and board.getPos(row, col) != '-'):
                    return board.getPos(row, col)

            #diagonal
            if (col <= 3 and row <= 2):
                if (board.getPos(row, col) == board.getPos(row + 1, col + 1) == board.getPos(row + 2, col + 2) == board.getPos(row + 3, col + 3) and board.getPos(row, col) != '-'):
                    return board.getPos(row, col)

            #diagonal
            if (col <= 3 and row >= 3):
                if (board.getPos(row, col) == board.getPos(row - 1, col + 1) == board.getPos(row - 2, col + 2) == board.getPos(row - 3, col + 3) and board.getPos(row, col) != '-'):
                    return board.getPos(row, col)
    return False

def possibleMoves(board: Board):
    # retorna uma lista com movimentos possiveis para a IA
    acc = []
    for i in range(7):
        position = testMoveValidity(board, i)
        if position != False:
            acc.append((i, position))
    return acc


