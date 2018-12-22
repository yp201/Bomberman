import numpy
from powerup import Powerup


class Wallpass(object):
    """class for Wallpass object"""

    def __init__(self, row, col, position_row, position_col, startTime):
        Powerup.__init__(self, row, col, position_row, position_col, startTime)
        self.symbol = 'W'

    def structure(self):
        WallpassStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return WallpassStructure
