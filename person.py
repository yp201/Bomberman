class Person:
    """class for Person object"""

    def __init__(self, row, col, position_row, position_col):
        self.row = row
        self.col = col
        self.position_row = position_row
        self.position_col = position_col
        self.cantMove = ("/", "X")

    def moveUp(self, gameBoard, emptySpace):
        dy = 2
        self.position_row = (self.position_row - dy) % 36
        if gameBoard[self.position_row][self.position_col] not in self.cantMove:
            if gameBoard[self.position_row][self.position_col] == 'X':
                dy = 4
                self.position_row = (self.position_row - 2) % 36
                if gameBoard[self.position_row][self.position_col] not in self.cantMove:
                    self.position_row = (self.position_row + dy) % 36
                    if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                        gameBoard[self.position_row:self.position_row + 2,
                                  self.position_col:self.position_col + 4] = emptySpace
                    self.position_row = (self.position_row - dy) % 36
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = self.structure()
                else:
                    self.position_row = (self.position_row + dy) % 36
            else:
                self.position_row = (self.position_row + 2) % 36
                if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = emptySpace
                self.position_row = (self.position_row - dy) % 36
                gameBoard[self.position_row:self.position_row + 2,
                          self.position_col:self.position_col + 4] = self.structure()
        else:
            self.position_row = (self.position_row + dy) % 36
        # if self.position_row==0:
            # self.position_row=(self.position_row-2)%36

    def moveDown(self, gameBoard, emptySpace):
        dy = 2
        self.position_row = (self.position_row + dy) % 36
        if gameBoard[self.position_row][self.position_col] not in self.cantMove:
            if gameBoard[self.position_row][self.position_col] == 'X':
                dy = 4
                self.position_row = (self.position_row + 2) % 36
                if gameBoard[self.position_row][self.position_col] not in self.cantMove:
                    self.position_row = (self.position_row - dy) % 36
                    if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                        gameBoard[self.position_row:self.position_row + 2,
                                  self.position_col:self.position_col + 4] = emptySpace
                    self.position_row = (self.position_row + dy) % 36
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = self.structure()
                else:
                    self.position_row = (self.position_row - dy) % 36
            else:
                self.position_row = (self.position_row - dy) % 36
                if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = emptySpace
                self.position_row = (self.position_row + dy) % 36
                gameBoard[self.position_row:self.position_row + 2,
                          self.position_col:self.position_col + 4] = self.structure()
        else:
            self.position_row = (self.position_row - dy) % 36

        # if self.position_row==0:
            # self.position_row=self.position_row+2

    def moveLeft(self, gameBoard, emptySpace):
        dx = 4
        self.position_col = (self.position_col - dx) % 72
        if gameBoard[self.position_row][self.position_col] not in self.cantMove:
            if gameBoard[self.position_row][self.position_col] == 'X':
                dx = 8
                self.position_col = (self.position_col - 4) % 72
                if gameBoard[self.position_row][self.position_col] not in self.cantMove:
                    self.position_col = (self.position_col + dx) % 72
                    if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                        gameBoard[self.position_row:self.position_row + 2,
                                  self.position_col:self.position_col + 4] = emptySpace
                    self.position_col = (self.position_col - dx) % 72
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = self.structure()
                else:
                    self.position_col = (self.position_col + dx) % 72

            else:
                self.position_col = (self.position_col + dx) % 72
                if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = emptySpace
                self.position_col = (self.position_col - dx) % 72
                gameBoard[self.position_row:self.position_row + 2,
                          self.position_col:self.position_col + 4] = self.structure()
        else:
            self.position_col = (self.position_col + dx) % 72

        # if self.position_col==0:
            # self.position_col=(self.position_col-4)%72

    def moveRight(self, gameBoard, emptySpace):
        dx = 4
        self.position_col = (self.position_col + dx) % 72
        if gameBoard[self.position_row][self.position_col] not in self.cantMove:
            if gameBoard[self.position_row][self.position_col] == 'X':
                dx = 8
                self.position_col = (self.position_col + 4) % 72
                if gameBoard[self.position_row][self.position_col] not in self.cantMove:
                    self.position_col = (self.position_col - dx) % 72
                    if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                        gameBoard[self.position_row:self.position_row + 2,
                                  self.position_col:self.position_col + 4] = emptySpace
                    self.position_col = (self.position_col + dx) % 72
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = self.structure()
                else:
                    self.position_col = (self.position_col - dx) % 72

            else:
                self.position_col = (self.position_col - dx) % 72
                if gameBoard[self.position_row][self.position_col] in ("B", "E", "<"):
                    gameBoard[self.position_row:self.position_row + 2,
                              self.position_col:self.position_col + 4] = emptySpace
                self.position_col = (self.position_col + dx) % 72
                gameBoard[self.position_row:self.position_row + 2,
                          self.position_col:self.position_col + 4] = self.structure()
        else:
            self.position_col = (self.position_col - dx) % 72
