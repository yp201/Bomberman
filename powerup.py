import numpy


class Powerup(object):
    """class for Powerup object"""

    def __init__(self, row, col, position_row, position_col, startTime):
        self.row = row
        self.col = col
        self.position_row = position_row
        self.position_col = position_col
        self.startTime = startTime
