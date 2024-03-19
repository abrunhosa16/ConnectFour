from copy import deepcopy

class Board:
    def __init__(self , player=None) -> None:
        self.board = []
        self.player = player

        for _ in range(6):
            row = []
            for _ in range(7):
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
    
    def __eq__(self , other) -> bool:
        for row in range(6):
            if self.board[row] != other.getRow(row):
                return False
        return True    
    
    def getRow(self , row:int) -> list:
        return self.board[row]
    
    def getPos(self , row:int , col:int) -> str:
        return self.board[row][col]
    
    def setPos(self , row:int , col:int) -> None:
        self.board[row][col] = self.player
        self.player = 'X' if self.player == 'O' else 'O'

    def resetBoard(self) -> None:
        for row in range(6):
            for col in range(7):
                self.board[row][col] = '-'

    def boardCopy(self):
        # se faz uma copia do tabuleiro no estado atual
        copy = Board()
        copy.board = deepcopy(self.board)
        copy.player = self.player
        return copy
    
    def finished(self) -> str | bool:
        for line in range(6):
            for col in range(7):
                if (line == 0):
                    row = self.getRow(line)
                    if (row.count('-') == 0): return 'Tie'
                    
                #horizontal
                if col <= 3:
                    if (self.getPos(line, col) == self.getPos(line, col + 1) == self.getPos(line, col + 2) == self.getPos(line, col + 3) and self.getPos(line, col) != '-'):
                        return self.getPos(line, col)
                #vertical
                if line <= 2:
                    if (self.getPos(line, col) == self.getPos(line + 1, col) == self.getPos(line + 2, col) == self.getPos(line + 3, col) and self.getPos(line, col) != '-'):
                        return self.getPos(line, col)
                #diagonal
                if (col <= 3 and line <= 2):
                    if (self.getPos(line, col) == self.getPos(line + 1, col + 1) == self.getPos(line + 2, col + 2) == self.getPos(line + 3, col + 3) and self.getPos(line, col) != '-'):
                        return self.getPos(line, col)
                #diagonal
                if (col <= 3 and line >= 3):
                    if (self.getPos(line, col) == self.getPos(line - 1, col + 1) == self.getPos(line - 2, col + 2) == self.getPos(line - 3, col + 3) and self.getPos(line, col) != '-'):
                        return self.getPos(line, col)
        return False
