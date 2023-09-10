# PythonSlowSnakeGame
Snake game (in CL) written in python without real time movement (every turn is based on player input)

The snake consists of a 9 and 1s, with the 9 representing the head. Since this game is turned based, a direction indicator is not required, but can be displayed if required since we remember the last direction we moved. The 2 represents the apple/food.

Moving requires typing out the direction you want to go (left, right, up or down). Enter Q to quit.

Current known bugs:
* At bigger lengths, an apple is not guaranteed to spawn, practically softlocking the game.
