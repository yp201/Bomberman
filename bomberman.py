import numpy
import sys
from person import Person


class Bomberman(Person):
    """class for Bomberman object"""

    def __init__(self, row, col, position_row, position_col, life, score):
        Person.__init__(self, row, col, position_row, position_col)
        self.symbol = 'B'
        self.life = life
        self.score = score
        self.powerUp = False
        self.powerUpStartTime = 0

    def structure(self):
        bomberManStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return bomberManStructure

    def die(self):
        sys.exit(0)
