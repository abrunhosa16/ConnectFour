import random


def generateBoard():
    board = []
    for i in range(6):
        vetor = []
        for j in range(7):
            vetor.append('-')
        board.append(vetor)
    return board

def printBoard(board):
    for k in range(7):
        print(k, end=" ")
    print("\n")
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print("\n")

def inputPlayer(letter):
    # define qual letra para cada jogador retorna [w, b] or [b, w]
    if letter == 'w':
        return ['w', 'b']
    else:
        return ['b', 'w']

def askForFirstPlayer():
    # perguntar ao jogador quem é que deve jogar primeiro, as opções
    #   podem ser por exemplo "white", "black" ou "random" e retorna o valor relacionado
    valid = False
    while not valid:
        piece = input("Queres ser w, b or r? ")
        if piece == "w" or piece == "b":
            return piece
        elif piece == "r":
            m = random.randint(0, 1)
            return "w" if m == 0 else "b"


def testMoveValidity(board, col):
    # testa se a jogada é válida se a casa esta vazia e qual a posição esta vazia
    # retorna a posição que esta vazia ou false
    for i in range(6):
        if board[5 - i][col] == "-":
            return 5 - i
    return False

#print(testMoveValidity([['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-']], 1))

def testMove(board, col):
    if col > 6 or col < 0:
        print("Fora das margens")
        return False

    position = testMoveValidity(board, col)

    if not position:
        print("Coluna não disponível")
        return False
    return position

#print(testMove([['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-']], 0))

def move(board, turn, col):
    position = testMove(board, col)
    if isinstance(position, int):
        board[position][col] = turn


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
            return (turn, move_col)




# print(askForNextMove([['-', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-'], ['w', '-', '-', '-', '-', '-', '-']], 'w'))

# # def winner(board):
# #     #retorna se algum jogador fez 4 em linha caso nao retorna falso
# #     raise (NotImplementedError)

def boardCopy(board):
    # se faz uma copia do tabuleiro no estado atual
    boardCopy = []
    for row in board:
        colCopy = []
        for col in row:
            colCopy.append(col)
        boardCopy.append(colCopy)
    return boardCopy


def availableMoveAi(board):
    # retorna uma lista com movimentos possiveis para a IA
    acc = []
    for i in range(7):
        position = testMoveValidity(board, i)
        if isinstance(position, int):
            acc.append((i, position))
    return acc


# def AIMove():
#     # executa o movimento da IA, supostamente aqui que implementaremos a IA
#     raise (NotImplementedError)

def main():
    board = generateBoard()
    start_p = askForFirstPlayer()

    if start_p == 'w':
        sec_p = 'b'
    else:
        sec_p = 'w'

    valid = True
    while valid or len(availableMoveAi) > 0:
        printBoard(board)
        print("First Player")
        moviment = askForNextMove(board, start_p)
        move(board, moviment[0], moviment[1])

        printBoard(board)
        print("Second Player")
        move_col2 = askForNextMove(board, sec_p)
        move(board, move_col2[0], move_col2[1])

        valid = True


if __name__ == '__main__':
    main()
