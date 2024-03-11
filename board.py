class Board:
    def __init__(self):
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
    
    def getRow(self, row) -> list:
        return self.board[row]
    
    def getPos(self, row, col) -> str:
        return self.board[row][col]
    
    def setPos(self, row, col, player):
        self.board[row][col] = player

    def resetBoard(self):
        for row in range(6):
            for col in range(7):
                self.board[row][col] = '-'

    def boardCopy(self):
        # se faz uma copia do tabuleiro no estado atual
        boardCopy = Board()
        for row in range(6):
            colCopy = []
            for col in range(7):
                boardCopy.setPos(row, col, self.getPos(row, col))
            boardCopy.board.append(colCopy)
        return boardCopy
    
    def finished(self):
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
