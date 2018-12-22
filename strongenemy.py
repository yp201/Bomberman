import numpy
from person import Person


class StrongEnemy(Person):
    """class for StrongEnemy object"""

    def __init__(self, row, col, position_row, position_col, number):
        Person.__init__(self, row, col, position_row, position_col)
        self.number = number
        self.health = 2
        self.symbol = '<'

    def structure(self):
        enemyStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return enemyStructure
