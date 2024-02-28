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
            string+= ''.join(str(i) + " ") 
        string+= '\n'
        
        for row in self.board:
            string += ' '.join(row) + '\n'
        return string
        
    def getPos(self, row, col):
            return self.board[row][col]
    
    def setPos(self, col, row, player):
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
    
    def getRow(self, row):
        return self.board[row]