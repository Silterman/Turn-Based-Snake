import random
from pprint import pprint

class snake:
    def __init__(self, size):
        self.body = [(int((size-1)/2),int((size-1)/2))]
        self.curDir = None
    def inputDetector(self, inp, game):
        turnTranslate = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right":[0, 1]}
        if self.validTurn(turnTranslate[inp]):
            self.curDir = turnTranslate[inp]
            self.move(game)
        else:
            print("Unable to U-Turn, choose another direction."); inp = str(input("What direction?")).lower()
            self.inputDetector(inp, game)
    def move(self, game): #moving snake coods
        #checking for snake collision
        if game.grid[(self.body[0][0]+self.curDir[0])%game.size][(self.body[0][1]+self.curDir[1])%game.size] == 1:
            print("Collision detected - GAME OVER!")
            quit()
        #checking for apple collision
        if game.grid[(self.body[0][0]+self.curDir[0])%game.size][(self.body[0][1]+self.curDir[1])%game.size] == 2:
            #replacing apple with snake part
            self.body.insert(0, ((self.body[0][0]+self.curDir[0])%game.size,(self.body[0][1]+self.curDir[1])%game.size)) 
            game.generateApple(self)
        game.grid[self.body[-1][0]%game.size][self.body[-1][1]%game.size] = 0 #setting tail on grid to 0 -> need to do it now while we still know coods
        for i in range(1, len(self.body)): #moving body one by one starting at the tail like a linked list
            self.body[-i] = self.body[-i-1]
        self.body[0] = (self.body[0][0]+self.curDir[0], self.body[0][1]+self.curDir[1]) #moving head based on direction
        self.updateGrid(game)
    def updateGrid(self, game) -> None: #redrawing grid/array
        for xy in self.body:
            game.grid[xy[0]%game.size][xy[1]%game.size] = 1
    def validTurn(self, inp) -> bool: #only checks if you do a uturn
        if self.curDir is None:
            return True
        if self.curDir[0]+inp[0] == 0 and self.curDir[1]+inp[1] == 0:
            return False
        return True
        

class gameGrid:
    def __init__(self, size, snake) -> None:
        self.size = size
        self.grid = [[0]*size for _ in range(size)]
        self.grid[snake.body[0][0]][snake.body[0][1]] = 1
        self.generateApple(snake)
    def generateApple(self, snake):
        x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
        if self.grid[x][y] != 1:
            self.grid[x][y] = 2
        else: self.generateApple(snake)

size = int(input("What size do you want to play with? Uneven integers only."))

player = snake(size)
game = gameGrid(size, player)

pprint(game.grid)

while True:
    inp = str(input("What direction?")).lower()
    if inp == "":
        print("Empty input detected, try again.")
        continue
    if inp == "q":
        quit()
    player.inputDetector(inp, game)
    pprint(game.grid)