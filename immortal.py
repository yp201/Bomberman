from powerup import Powerup
import numpy


class Immortal (object):
    """class for Immortal object"""

    def __init__(self, row, col, position_row, position_col, startTime):
        Powerup.__init__(self, row, col, position_row, position_col, startTime)
        self.symbol = 'I'

    def structure(self):
        ImmortalStructure = numpy.asarray([[self.symbol] * 4] * 2)
        return ImmortalStructure
