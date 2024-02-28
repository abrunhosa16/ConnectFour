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

def boardCopy(board):
    # se faz uma copia do tabuleiro no estado atual
    boardCopy = []
    for row in board:
        colCopy = []
        for col in row:
            colCopy.append(col)
        boardCopy.append(colCopy)
    return boardCopy