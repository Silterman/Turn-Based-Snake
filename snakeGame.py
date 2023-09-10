import random
from pprint import pprint

#to do
# make it clear where the head of the snake is

class snake:
    def __init__(self, size):
        self.body = [(int((size-1)/2),int((size-1)/2))]
        self.curDir = [0,0]
        self.score = 0
    def inputDetector(self, inp, game):
        turnTranslate = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right":[0, 1]}
        if self.validTurn(turnTranslate[inp]):
            self.curDir = turnTranslate[inp]
            self.move(game)
        else:
            print("Unable to U-Turn, choose another direction."); inp = str(input("What direction?")).lower()
            self.inputDetector(inp, game)
    def move(self, game): #moving snake coods
        aCollision=False
        #checking for snake collision
        if game.grid[(self.body[0][0]+self.curDir[0])%game.size][(self.body[0][1]+self.curDir[1])%game.size] == 1:
            print("Collision detected - GAME OVER!")
            print("Score:", self.score)
            quit()
        #checking for apple collision
        if game.grid[(self.body[0][0]+self.curDir[0])%game.size][(self.body[0][1]+self.curDir[1])%game.size] == 2:
            aCollision = self.body[-1]
            self.score += 1
        game.grid[self.body[-1][0]%game.size][self.body[-1][1]%game.size] = 0 #setting tail on grid to 0 -> need to do it now while we still know coods
        for i in range(1, len(self.body)): #moving body one by one starting at the tail like a linked list
            self.body[-i] = self.body[-i-1]
        self.body[0] = (self.body[0][0]+self.curDir[0], self.body[0][1]+self.curDir[1]) #moving head based on direction
        if aCollision:
            self.body.append(aCollision)
        game.updateGrid(self)
        if aCollision: #need to do this after moving the snake, otherwise there is a chance the movement replaces the new apple.
            game.generateApple(self)
    def validTurn(self, inp) -> bool: #only checks if you do a uturn
        if self.curDir[0]+inp[0] == 0 and self.curDir[1]+inp[1] == 0:
            return False
        return True
        

class gameGrid:
    def __init__(self, size, snake) -> None:
        self.size = size
        self.grid = [[0]*size for _ in range(size)]
        self.grid[snake.body[0][0]][snake.body[0][1]] = 9
        self.generateApple(snake)
    def generateApple(self, snake):
        x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
        if (x, y) not in snake.body:
            self.grid[x][y] = 2
        else: self.generateApple(snake)
    def updateGrid(self, snake) -> None: #redrawing grid/array
        self.grid[snake.body[0][0]%self.size][snake.body[0][1]%self.size] = 9
        for xy in snake.body[1:]:
            self.grid[xy[0]%self.size][xy[1]%self.size] = 1

size = int(input("What size do you want to play with? Uneven integers only."))

player = snake(size)
game = gameGrid(size, player)

pprint(game.grid)

while True:
    inp = str(input("What direction?")).lower()
    if inp not in ["up", "down", "right", "left", "q"]:
        print("Incorrect input detected, try again.")
        continue
    if inp == "q":
        print("Quitting. Your score is", str(player.score)+".")
        quit()
    player.inputDetector(inp, game)
    pprint(game.grid)
