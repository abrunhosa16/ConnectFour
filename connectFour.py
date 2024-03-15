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

def askForAlgorithm():
    while True:
        try:
            algorithm = int(input("Qual algoritmo queres? 1 - P vs P, 2 - A*, 3 - MC, 4 - MinMAx : "))
        except ValueError:
            print("Tente inteiros. \n")
            continue

        if algorithm in range(1, 5, 1):
            return algorithm
        else:
            print('Tente um número de 1 a 4. \n')
        
def playAgain():
    while True:
        play = input(("Queres jogar de novo? S ou N. : "))
        if play.upper() == 'S':
            return True
        elif play.upper() == 'N':
            return False
        else:
            print('Tente S ou N. \n')

def testMoveValidity(board: Board, col) -> int | bool:
    # testa se a jogada é válida se a casa esta vazia e qual a posição esta vazia
    # retorna a posição que esta vazia ou false
    for i in range(6):
        if board.getPos(5-i, col) == "-":
            return 5 - i
    return -1

def fullyBoard(board):
    return all(board[0][col] != '-' for col in range(7))

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
                
            if (row == 0):
                line = board.getRow(row)
                if (line.count('-') == 0): return 'Tie'
    return False

# def horizontal_check(board: Board, row, col, turn: str) -> int:
#   acc = 1  
#   for i in range(col + 1, 7):  # Limit to 6 (valid column index)
#     if board.getPos(row, i) != turn:
#       break
#     acc += 1
#   for i in range(col - 1, 0, -1):
#     if board.getPos(row, i) != turn:
#       break
#     acc += 1
#   return acc

# def vertical_check(board: Board, row, col, turn: str) -> int:
  
#   acc = 1 
#   for i in range(1, row + 1): 
#     if board.getPos(row - i, col) != turn:
#       break
#     acc += 1
#   for i in range(1, 5 - row):
#     if board.getPos(row + i + 1, col) != turn:
#       break
#     acc += 1
#   return acc

# def diag_left_to_right_down(board: Board, row: int, col: int, turn: str) -> int:
#   acc = 1  
#   for i in range(1, min(5 - row, 6 - col)):
#     if board.getPos(row + i, col + i) != turn:
#       break
#     acc += 1
    
#   for i in range(1, min(row + 1, col + 1)):
#     if board.getPos(row - i, col - i) != turn:
#       break
#     acc += 1

#   print(acc)
#   return acc

# def diag_left_to_right_up(board: Board, row: int, col: int, turn: str) -> int:
#   acc = 1  
#   for i in range(1, min(5 - row, col + 1)):
#     if board.getPos(row + i, col - i) != turn:
#       break
#     acc += 1
#   for i in range(1, min(row + 1, 6 - col)):
#     if board.getPos(row - i , col + i) != turn:
#       break
#     acc += 1
#   return acc

# def winner2(board: Board, row, col, turn):

#     if horizontal_check(board, row, col, turn) >= 4:
#         return True
    
#     elif vertical_check(board, row, col, turn) >= 4:
#         return True
    
#     elif diag_left_to_right_down(board, row, col, turn) >= 5:
#         return True
    
#     elif diag_left_to_right_up(board, row, col, turn) >= 5:
#         return True
    
#     return False
    


          
# # tab2 = Board()
# # tab2.setPos(5,0,'X')
# # tab2.setPos(5,1,'X')
# # tab2.setPos(5,2,'X')
# # tab2.setPos(5,5,'O')
# # tab2.setPos(4,5,'O')
# # print(tab2)
# # print(left(tab2, [5, 0], 'X'))




def possibleMoves(board: Board):
    # retorna uma lista com movimentos possiveis para a IA
    acc = []
    for i in range(7):
        position = testMoveValidity(board, i)
        if position != -1:
            acc.append((position, i))
    return acc

def gamePerson(board: Board, player):
    turn, col, line = askForNextMove(board, player)
    move(board, turn, col, line)
