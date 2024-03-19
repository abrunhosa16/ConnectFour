from connectFour import possibleMoves, askForNextMove, winnerAi
from board import Board

def get_line_points_original(line:list, player:str) -> int:
    if (line.count('X') == 3 and line.count('O') == 0): 
        return 50
    if (line.count('X') == 2 and line.count('O') == 0): 
        return 10
    if (line.count('X') == 1 and line.count('O') == 0): 
        return 1
    if (line.count('X') == 0 and line.count('O') == 3):
        return -50
    if (line.count('X') == 0 and line.count('O') == 2):
        return -10
    if (line.count('X') == 0 and line.count('O') == 1): 
        return -1
    return 0

def get_line_points_modidfied(line:list , player:str) -> int:
    opponent = 'X' if player == 'O' else 'O'
    if (line.count('X') == 3 and line.count('O') == 0): 
        if 'X' == opponent: return 250
        else: return 50
    if (line.count('X') == 2 and line.count('O') == 0): 
        if 'X' == opponent: return 50
        else: return 10
    if (line.count('X') == 1 and line.count('O') == 0): 
        return 1
    if (line.count('X') == 0 and line.count('O') == 3):
        if 'O' == opponent: return -250
        else: return -50
    if (line.count('X') == 0 and line.count('O') == 2):
        if 'O' == opponent: return -50
        else: return -10
    if (line.count('X') == 0 and line.count('O') == 1): 
        return -1
    return 0

def getPoints(board:Board , player:str , getLinePoints) -> int:
    win = board.finished()
    if win == 'X': return 512
    if win == 'O': return -512
    if win == 'Tie': return 0
    points = 16 if player == 'X' else -16
    for line in range(6):
        for col in range(7):
            #horizontal
            if col < 4:
                points += getLinePoints( [board.getPos(line, col+i) for i in range(4)], player)

            #vertical
            if line < 3:
                points += getLinePoints( [board.getPos(line + i, col) for i in range(4)], player)
                
            #diagonal positiva
            if line < 3 and col < 4:
                points += getLinePoints( [board.getPos(line + i, col + i) for i in range(4)], player)

            #diagonal negativa
            if line > 2 and col < 4:
                points += getLinePoints( [board.getPos(line - i, col + i) for i in range(4)], player)
    return points

def Astar(state:Board , getLinePoints) -> list:
    ai = state.player
    moves = possibleMoves(state)
    best_move = [state, getPoints(state, ai, getLinePoints), -1, -1]
    for line, col in moves:
        new_state = state.boardCopy()
        new_state.setPos(line, col)
        new_state_points = getPoints(new_state, ai, getLinePoints)
        if ai == 'X':
            if new_state_points == 512:
                return [new_state, line, col]
            if new_state_points > best_move[1]:
                best_move = [new_state, new_state_points, line, col]
        else:
            if new_state_points == -512:
                return [new_state, line, col]
            if new_state_points < best_move[1]:
                best_move = [new_state, new_state_points, line, col]
    
    #para verificar se ela não joga         
    if state == best_move[0]:
        print('-------------------------------------------------------------------------------------------')
        
    return [best_move[0], best_move[2], best_move[3]]

def gameAstar(board:Board , order:list) -> None:
    while True: 
        try:
            option = int(input('Queres jogar com que heurística? 1 - Original, 2 - Modificada: '))
        except ValueError:
            print('Tente 1 ou 2. \n')
            continue
        if option == 1:
            get_line_points = get_line_points_original
            break
        elif option == 2:
            get_line_points = get_line_points_modidfied
            break
        else:
            print('Tente 1 ou 2. \n')
    print(board)
    while True:
        print('Tua vez.')
        _, col = askForNextMove(board)
        print(board)
        
        if winnerAi(board, order):
            return
        
        board, _, col = Astar(board, get_line_points)
        print('A IA pôs uma peça na coluna ' + str(col) + '.')
        print(board)
        
        if winnerAi(board, order):
            return
       