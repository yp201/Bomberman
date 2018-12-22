import numpy


class Bomb(object):
    """class for Bomb object"""

    def __init__(self, row, col, position_row, position_col):
        self.row = row
        self.col = col
        self.timer = 3
        self.symbol = 'O'
        self.position_row = position_row
        self.position_col = position_col
        self.explosion_row = 2
        self.explosion_col = 4

    def structure(self):
        bombStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return bombStructure

    def show(self, gameBoard):
        gameBoard[self.position_row:self.position_row + 2,
                  self.position_col:self.position_col + 4] = self.structure()

    def countDown(self, gameBoard):
        gameBoard[self.position_row:self.position_row + 2,
                  self.position_col:self.position_col + 4] = numpy.asarray([[str(self.timer)] * 4] * 2)

    def explode(self, gameBoard, bomberman):
        explosionStructure = numpy.asarray([['e'] * 4] * 2)
        explosions = []
        explosions.append([self.position_row , self.position_col])
        if gameBoard[self.position_row - 2][self.position_col] not in ("X","I","W"):
            if gameBoard[self.position_row + 2][self.position_col] == '/':
                bomberman.score += 50
            gameBoard[self.position_row - 2:self.position_row,
                      self.position_col:self.position_col + 4] = explosionStructure
            explosions.append([self.position_row - 2, self.position_col])
        if gameBoard[self.position_row + 2][self.position_col] not in ("X","I","W"):
            if gameBoard[self.position_row + 2][self.position_col] == '/':
                bomberman.score += 50
            gameBoard[self.position_row + 2:self.position_row + 4,
                      self.position_col:self.position_col + 4] = explosionStructure
            explosions.append([self.position_row + 2 , self.position_col])
        if gameBoard[self.position_row][self.position_col - 4] not in ("X","I","W"):
            if gameBoard[self.position_row][self.position_col - 4] == '/':
                bomberman.score += 50
            gameBoard[self.position_row:self.position_row + 2,
                      self.position_col - 4:self.position_col] = explosionStructure
            explosions.append([self.position_row , self.position_col - 4])
        if gameBoard[self.position_row][self.position_col + 4] not in ("X","I","W"):
            if gameBoard[self.position_row][self.position_col + 4] == '/':
                bomberman.score += 50
            gameBoard[self.position_row:self.position_row + 2,
                      self.position_col + 4:self.position_col + 8] = explosionStructure
            explosions.append([self.position_row , self.position_col + 4])
        return explosions

    def removeResidue(self, gameBoard, emptySpace):
        gameBoard[self.position_row:self.position_row + 2,
                  self.position_col:self.position_col + 4] = emptySpace
        if gameBoard[self.position_row - 2][self.position_col] == 'e':
            gameBoard[self.position_row - 2:self.position_row,
                      self.position_col:self.position_col + 4] = emptySpace
        if gameBoard[self.position_row + 2][self.position_col] == 'e':
            gameBoard[self.position_row + 2:self.position_row + 4,
                      self.position_col:self.position_col + 4] = emptySpace
        if gameBoard[self.position_row][self.position_col - 4] == 'e':
            gameBoard[self.position_row:self.position_row + 2,
                      self.position_col - 4:self.position_col] = emptySpace
        if gameBoard[self.position_row][self.position_col + 4] == 'e':
            gameBoard[self.position_row:self.position_row + 2,
                      self.position_col + 4:self.position_col + 8] = emptySpace
