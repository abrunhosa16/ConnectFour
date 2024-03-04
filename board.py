class Board:
    def __init__(self):
        self.board = []

        for i in range(6):
            vetor = []
            for j in range(7):
                vetor.append('-')
            self.board.append(vetor)
        
    def __str__(self):
        string = ''
        for i in range(7):
            string += ''.join(str(i) + " ") 
        string+= '\n'
        
        for row in range(6):  
            string += ' '.join(self.board[row]) + '\n'
        return string
        
    def getRow(self, row):
        return self.board[row]
    
    def __eq__(self, other):
        for row in range(6):
            if self.board[row] != other.getRow(row):
                return False
        return True
    
    def resetBoard(self):
        for row in range(6):
            for col in range(7):
                self.board[row][col] = '-'

    def getPos(self, row, col):
            return self.board[row][col]
    
    def setPos(self, row, col, player):
        self.board[row][col] = player

    def boardCopy(self):
        # se faz uma copia do tabuleiro no estado atual
        boardCopy = Board()
        for row in range(6):
            colCopy = []
            for col in range(7):
                boardCopy.setPos(row, col, self.getPos(row, col))
            boardCopy.board.append(colCopy)
        return boardCopy