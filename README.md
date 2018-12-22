BOMBERMAN
DEVELOPED BY YASHASWI PATHAK (20161149)

Welcome to the terminal based game Bomberman(developed in python3).

To start the game first install all the requirements from requirements.txt, then in the directory type python3 run.py.

In this game Bomberman has to kill all the enemies to move to the next level.Difficulty of the game increases with levels.

Controls:

W - Move Up
A - Move Left
S - Move Down
D - Move right
B - Plant Bomb
P - Powerup
Q - Quit

Enemies:

Enemies  are spawned at random locations. You need to plant bombs when near them to kill them.There are two types of enemies.On killing one enemy bomberman gets 100 point.No. of enemies increses with levels

Bricks:

Bricks  are spawned at random locations. You need to plant bombs when near them to destroy them.On destroying one brick bomberman gets 50 point.No. of bricks increase with levels


Bombs:
(on key-press 'B')

Bombs are planted by pressing the key 'b', it takes 3 frames for a bomb to  explode, its effect goes to all the places adjacent to it (horizontally or vertically), except powerups and walls

Powerups(BONUS):
(on key-press 'P')

Powerups are spawned at random location and stays there for 10 sec if the bomberman is unable to collect it and then disappears.If the bomberman collects the powerup it affect lasts for 10 seconds.

There are two types of powerups:
	1)Immortal:Bomberman becomes Immortal
	2)Wallpass:BOmberman can pass through wall

GAME DESIGN:

OOPS concepts such as Modularity, Inheritance, Encapsulation and Polymorphism have been kept in mind at every step of implementation.

Classes present:
Person
Bomberman
Enemy
Strongenemy	
Bomb
Wall
Brick
Board
Powerup
Immortal
Wallpass

The game has been run on a terminal of Black Background, Please consider that will running game.

Note:
-Desing of the board can be changed by going to run.py and configuring(or changing) rows,cols,etc.
-All the bonus part has been implemented.

Hope you enjoy the game.
Thankyou for playing.