import os
import sys
import numpy
import random
from person import Person
from enemy import Enemy
from strongenemy import StrongEnemy
from immortal import Immortal
from wallpass import Wallpass
from wall import Wall
from brick import Brick
from colored import fore, style
import time


class Board:
    """class for Board object"""

    def __init__(self, row, col, fps):

        self.row = row
        self.col = col
        self.timer = 0
        self.gameBoard = numpy.asarray([[' '] * self.col] * self.row)
        self.fps = fps
        self.enemies = []
        self.bricks = []
        self.bombs = []
        self.currentExplosions = []
        self.powerUps = []
        self.newGame = False
        self.level = 1

    def initialise(self, bomberman, wall):

        self.newGame = False
        self.timer = 0
        bomberman.immortal = False
        bomberman.powerUp = False
        bomberman.cantMove = ("/", "X")
        bomberman.position_row = 2
        bomberman.position_col = 4
        self.gameBoard = numpy.asarray([[' '] * self.col] * self.row)
        self.enemies = []
        self.bombs = []
        self.bricks = []
        self.gameBoard[
            bomberman.position_row:bomberman.position_row + 2,
            bomberman.position_col:bomberman.position_col + 4
            ] = bomberman.structure()

        for i in range(0, self.row, 2):
            for j in range(0, self.col, 4):
                if i == 0 or i == 36:
                    self.gameBoard[i:i + 2, j:j + 4] = wall.structure()
                elif (i != 0 or i != 38) and (j == 0 or j == 72):
                    self.gameBoard[i:i + 2, j:j + 4] = wall.structure()
                elif (i % 4 == 0) and (j % 8 == 0):
                    self.gameBoard[i:i + 2, j:j + 4] = wall.structure()
        counter = 0

        while(counter < 1 * self.level):
            enemy_row = random.randrange(2, 37, 2)
            enemy_col = random.randrange(4, 69, 4)
            if (self.gameBoard[enemy_row][enemy_col] == " " and
               ((enemy_row, enemy_col) not in ((4, 4), (2, 8)))):
                self.enemies.append(Enemy(2, 4, enemy_row, enemy_col, counter))
                self.gameBoard[
                        enemy_row:enemy_row + 2,
                        enemy_col:enemy_col + 4
                        ] = self.enemies[-1].structure()
                counter += 1

        counter = 0

        while(counter < 1 * self.level):
            strongenemy_row = random.randrange(2, 37, 2)
            strongenemy_col = random.randrange(4, 69, 4)
            if (self.gameBoard[strongenemy_row][strongenemy_col] == " " and
               ((strongenemy_row, strongenemy_col) not in ((4, 4), (2, 8)))):
                self.enemies.append(StrongEnemy(
                    2, 4, strongenemy_row, strongenemy_col, counter))
                self.gameBoard[
                        strongenemy_row:strongenemy_row + 2,
                        strongenemy_col:strongenemy_col + 4
                        ] = self.enemies[-1].structure()
                counter += 1

        counter = 0

        while(counter < 8 + self.level):
            brick_row = random.randrange(2, 37, 2)
            brick_col = random.randrange(4, 69, 4)
            if (self.gameBoard[brick_row][brick_col] == " " and
               ((brick_row, brick_col) not in ((4, 4), (2, 8)))):
                self.bricks.append(Brick(2, 4))
                self.gameBoard[
                        brick_row:brick_row + 2,
                        brick_col:brick_col + 4
                        ] = self.bricks[counter].structure()
                counter += 1

        self.__printing(bomberman)

    def __moveEnemy(self, emptySpace):

        if self.timer % 1 == 0:

            for enemy in self.enemies:
                if enemy.health > 0:
                    direction = random.choice('wasd')
                    if direction == 'w':
                        enemy.moveUp(self.gameBoard, emptySpace)
                    elif direction == 'd':
                        enemy.moveRight(self.gameBoard, emptySpace)
                    elif direction == 'a':
                        enemy.moveLeft(self.gameBoard, emptySpace)
                    elif direction == 's':
                        enemy.moveDown(self.gameBoard, emptySpace)

    def __bombExplosions(self, bomberman, emptySpace):
        for bomb in self.bombs:
            if bomb.timer == 0:
                self.currentExplosions = bomb.explode(
                    self.gameBoard, bomberman)
                bomb.timer = bomb.timer - 1
            elif bomb.timer == -1:
                bomb.removeResidue(self.gameBoard, emptySpace)
                bomb.timer = bomb.timer - 1
            elif bomb.timer > 0:
                bomb.countDown(self.gameBoard)
                bomb.timer = bomb.timer - 1

    def __deathDueToEnemies(self, bomberman, wall):
        if bomberman.immortal is not True:
            for enemy in self.enemies:
                if enemy.health > 0:
                    if (bomberman.position_row == enemy.position_row and
                       bomberman.position_col == enemy.position_col):
                        bomberman.life = bomberman.life - 1
                        if bomberman.life > 0:
                            self.newGame = True
                            print("TRY AGAIN")
                            time.sleep(2)
                            self.initialise(bomberman, wall)
                        else:
                            print("GAME OVER")
                            bomberman.die()

    def __deathDueToBombs(self, bomberman, wall):
        for i in range(len(self.currentExplosions)):

            if bomberman.immortal is not True:
                if ((self.currentExplosions[i][0],
                   self.currentExplosions[i][1]) ==
                   (bomberman.position_row, bomberman.position_col)):
                    bomberman.life -= 1

                    if bomberman.life > 0:
                        self.newGame = True
                        print("TRY AGAIN")
                        time.sleep(2)
                        self.initialise(bomberman, wall)

                    else:
                        print("GAME OVER")
                        bomberman.die()

            for enemy in self.enemies:
                if enemy.health > 0:
                    if ((self.currentExplosions[i][0],
                       self.currentExplosions[i][1]) ==
                       (enemy.position_row, enemy.position_col)):
                        enemy.health = enemy.health - 1
                        if enemy.health < 1:
                            enemy.position_row = -2
                            enemy.position_col = -2
                            bomberman.score += 100

    def __nextLevel(self, bomberman, wall):
        nextLevel = True
        for enemy in self.enemies:
            if enemy.health > 0:
                nextLevel = False
        if nextLevel is True:
            self.level += 1
            print("you are going to next level")
            time.sleep(2)
            self.initialise(bomberman, wall)

    def __checkState(self, bomberman):
        if self.newGame is not True:
            self.__printing(bomberman)

    def __checkPowerUp(self, bomberman, emptySpace):

        if bomberman.powerUp is not True:

            for powerUp in self.powerUps:

                if ((powerUp.position_row,
                   powerUp.position_col) ==
                   (bomberman.position_row, bomberman.position_col)):
                    bomberman.powerUp = True

                    if powerUp.symbol == 'I':
                        bomberman.immortal = True
                    elif powerUp.symbol == 'W':
                        bomberman.cantMove = ("/")

                    bomberman.powerUpStartTime = time.time()

                if time.time() - powerUp.startTime > 10:
                    self.gameBoard[powerUp.position_row:
                                   powerUp.position_row + 2,
                                   powerUp.position_col:
                                   powerUp.position_col + 4] = emptySpace
                    self.powerUps = []
                    # break
        elif bomberman.powerUp is True:

            if time.time() - bomberman.powerUpStartTime > 10:

                bomberman.powerUp = False
                bomberman.immortal = False
                bomberman.cantMove = ("/", "X")
                self.powerUps = []

    def powerUp(self):

        powerUp = random.choice("WI")
        while self.powerUps == []:

            counter = 0
            powerup_row = random.randrange(2, 37, 2)
            powerup_col = random.randrange(4, 69, 4)
            if self.gameBoard[powerup_row][powerup_col] == " ":
                if powerUp == 'I':
                    self.powerUps.append(
                        Immortal(2, 4, powerup_row, powerup_col, time.time()))
                elif powerUp == 'W':
                    self.powerUps.append(
                        Wallpass(2, 4, powerup_row, powerup_col, time.time()))

                self.gameBoard[powerup_row:
                               powerup_row + 2,
                               powerup_col:
                               powerup_col + 4] = self.powerUps[-1].structure()
        return

    def operate(self, bomberman, wall, emptySpace):
        self.timer += (0.25 * self.level)
        self.currentExplosions.clear()
        self.__moveEnemy(emptySpace)
        self.__deathDueToEnemies(bomberman, wall)
        self.__bombExplosions(bomberman, emptySpace)
        self.__deathDueToBombs(bomberman, wall)
        self.__checkPowerUp(bomberman, emptySpace)
        self.__nextLevel(bomberman, wall)
        self.__checkState(bomberman)

    def __printing(self, bomberman):
        os.system('clear')
        for i in range(self.row):
            for j in range(self.col):
                if self.gameBoard[i][j] == 'E':
                    print(fore.RED + self.gameBoard[i]
                          [j], end="" + style.RESET)
                elif self.gameBoard[i][j] == '<':
                    print(fore.YELLOW +
                          self.gameBoard[i][j], end="" + style.RESET)
                elif self.gameBoard[i][j] == 'X':
                    print(fore.GREEN +
                          self.gameBoard[i][j], end="" + style.RESET)
                elif self.gameBoard[i][j] == 'B':
                    print(fore.BLUE +
                          self.gameBoard[i][j], end="" + style.RESET)
                elif self.gameBoard[i][j] == 'I':
                    print(fore.CYAN +
                          self.gameBoard[i][j], end="" + style.RESET)
                elif self.gameBoard[i][j] == 'W':
                    print(fore.MAGENTA +
                          self.gameBoard[i][j], end="" + style.RESET)
                else:
                    print(self.gameBoard[i][j], end="")
            print("")
        print("LEVEL = " + str(self.level) + "\tPOWERUP = " +
              str(bomberman.powerUp) + "\t\tSCORE = " +
              str(bomberman.score) + "\tLIFES = " +
              str(bomberman.life))
