import numpy
from person import Person


class Enemy(Person):
    """class for Enemy object"""

    def __init__(self, row, col, position_row, position_col, number):
        Person.__init__(self, row, col, position_row, position_col)
        self.symbol = 'E'
        self.number = number
        self.health = 1

    def structure(self):
        enemyStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return enemyStructure
