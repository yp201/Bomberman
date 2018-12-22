import numpy


class Wall(object):
    """class for Wall object"""

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.symbol = 'X'

    def structure(self):
        wallStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return wallStructure
