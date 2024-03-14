from copy import deepcopy

class Board:
    def __init__(self) -> None:
        self.board = []

        for i in range(6):
            row = []
            for j in range(7):
                row.append('-')
            self.board.append(row)
        
    def __str__(self) -> str:
        string = ''
        for i in range(7):
            string += ''.join(str(i) + " ") 
        string+= '\n'
        
        for row in range(6):  
            string += ' '.join(self.board[row]) + '\n'
        return string
    
    def __eq__(self, other) -> bool:
        for row in range(6):
            if self.board[row] != other.getRow(row):
                return False
        return True    
    
    def getRow(self, row:int) -> list:
        return self.board[row]
    
    def getPos(self, row:int, col:int) -> str:
        return self.board[row][col]
    
    def setPos(self, row:int, col:int, player:str) -> None:
        self.board[row][col] = player

    def resetBoard(self) -> None:
        for row in range(6):
            for col in range(7):
                self.board[row][col] = '-'

    def boardCopy(self):
        # se faz uma copia do tabuleiro no estado atual
        copy = Board()
        copy.board = deepcopy(self.board)
        return copy
    
    def finished(self) -> str | bool:
        for row in range(6):
            for col in range(7):
                
                #horizontal
                if col <= 3:
                    if (self.getPos(row, col) == self.getPos(row, col + 1) == self.getPos(row, col + 2) == self.getPos(row, col + 3) and self.getPos(row, col) != '-'):
                        return self.getPos(row, col)
                #vertical
                if row <= 2:
                    if (self.getPos(row, col) == self.getPos(row + 1, col) == self.getPos(row + 2, col) == self.getPos(row + 3, col) and self.getPos(row, col) != '-'):
                        return self.getPos(row, col)
                #diagonal
                if (col <= 3 and row <= 2):
                    if (self.getPos(row, col) == self.getPos(row + 1, col + 1) == self.getPos(row + 2, col + 2) == self.getPos(row + 3, col + 3) and self.getPos(row, col) != '-'):
                        return self.getPos(row, col)
                #diagonal
                if (col <= 3 and row >= 3):
                    if (self.getPos(row, col) == self.getPos(row - 1, col + 1) == self.getPos(row - 2, col + 2) == self.getPos(row - 3, col + 3) and self.getPos(row, col) != '-'):
                        return self.getPos(row, col)
                    
                if (row == 0):
                    line = self.getRow(row)
                    if (line.count('-') == 0): return 'Tie'
        return False

    def finished_from(self, row:int, col:int) -> str | bool:
        #verifica apenas as linhas que incluem a casa onde foi jogada uma peça
        if self.getRow(0).count('-') == 0:
            return 'Tie'
        
        #horizontal
        limits_col = [max(0, col-3), min(6, col+3)]
        sequence = [self.getPos(row, limits_col[0]), 0]
        for i in range(limits_col[0], limits_col[1] + 1, 1):
            if self.getPos(row, i) != sequence[0]:
                sequence = [self.getPos(row, i), 1]
            else:
                sequence[1] += 1
            if (sequence[1] == 4 and sequence[0] != '-'):
                return self.getPos(row, col)
            
        #vertical
        limits_row = [max(0, row-3), min(5, row+3)]
        sequence = [self.getPos(row, limits_row[0]), 0]
        for i in range(limits_row[0], limits_row[1] + 1, 1):
            if self.getPos(i, col) != sequence[0]:
                sequence = [self.getPos(i, col), 1]
            else:
                sequence[1] += 1
            if (sequence[1] == 4 and sequence[0] != '-'):
                return self.getPos(row, col)
            
        #vertical e-d c-b
        interval = min(limits_row[1] - limits_row[0], limits_col[1] - limits_col[0]) #numero de casas da diagonal a ver
        sequence = [self.getPos(limits_row[0], limits_col[0]), 0]
        for i in range(interval):
            if self.getPos(limits_row[0] + i, limits_col[0] + i) != sequence[0]:
                sequence = [self.getPos(limits_row[0] + i, limits_col[0] + i), 1]
            else:
                sequence[1] += 1
            if (sequence[1] == 4 and sequence[0] != '-'):
                return self.getPos(row, col)
            
        #vertical e-d b-c
        sequence = [self.getPos(limits_row[0], limits_col[0]), 0]
        for i in range(interval):
            if self.getPos(limits_row[1] - i, limits_col[0] + i) != sequence[0]:
                sequence = [self.getPos(limits_row[1] - i, limits_col[0] + i), 1]
            else:
                sequence[1] += 1
            if (sequence[1] == 4 and sequence[0] != '-'):
                return self.getPos(row, col)
        
        return False