import numpy
from getch import get_char
import random
import time
from board import Board
from person import Person
from enemy import Enemy
from bomberman import Bomberman
from wall import Wall
from brick import Brick
from bomb import Bomb

board = Board(38, 76, 0.1)
bomberman = Bomberman(2, 4, 2, 4, 3, 0)
emptySpace = numpy.asarray([[' '] * 4] * 2)
wall = Wall(2, 4)
fps = board.fps


board.initialise(bomberman, wall)


def render():
    playerInput = "none"
    playerInput = get_char()
    time.sleep(fps)

    # player input #
    if playerInput in ("W","w"):
        bomberman.moveUp(board.gameBoard, emptySpace)
    elif playerInput in ("D","d"):
        bomberman.moveRight(board.gameBoard, emptySpace)
    elif playerInput in ("A","a"):
        bomberman.moveLeft(board.gameBoard, emptySpace)
    elif playerInput in ("S","s"):
        bomberman.moveDown(board.gameBoard, emptySpace)
    elif playerInput in ("B","b"):
        board.bombs.append(
            Bomb(2, 4, bomberman.position_row, bomberman.position_col))
        board.bombs[-1].show(board.gameBoard)
    elif playerInput in ("P","p"):
        board.powerUp()
    elif playerInput in ("Q","q"):
        print("BYE BYE ,SEE YOU SOON")
        bomberman.die()
    elif playerInput is None:
        pass
    # player input #

    board.operate(bomberman, wall, emptySpace)

while(True):
    render()
