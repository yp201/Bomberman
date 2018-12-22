import numpy


class Brick(object):
    """class for Brick object"""

    def __init__(self, row, col):

        self.row = row
        self.col = col
        self.symbol = '/'

    def structure(self):
        BrickStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return BrickStructure
