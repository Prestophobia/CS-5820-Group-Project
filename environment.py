import random

from states import *

CLEAN_WEIGHT = 1
STEPS_WEIGHT = 0.2

class Environment:
    Grid = []
    Width = 0
    Height = 0
    NumCollisions = 0
    NumTurns = 0
    InitialDirtyAmount = 0

    def __init__(self,width,height):
        self.Width = width
        self.Height = height
        self.Grid = []
        for x in range(width):
            newCol = []
            for y in range(height):
                newCol.append(CLEAN)
            self.Grid.append(newCol)

    def Reset(self):
        self.NumCollisions = 0
        self.NumTurns = 0
        self.RandomizeWithoutWalls()

    def GetTile(self,x,y):
        if x >= self.Width or y >= self.Height or x < 0 or y < 0:
            return WALL
        else:
            return self.Grid[x][y]

    def SetTile(self,x,y,val):
        #assert self.Grid[x][y] == WALL and not val == WALL
        self.Grid[x][y] = val

    def SetTileByNumber(self,tileNumber,val):
        y = int(tileNumber/self.Width)
        x = int(tileNumber%self.Width)
        self.SetTile(x,y,val)

    def SetGridFromBinary(self,bin):
        self.NumCollisions = 0
        self.NumTurns = 0
        number = bin
        binDigits = self.Width * self.Height
        for b in range(0,binDigits):
            if (number%2 != 0):
                self.SetTileByNumber(b,DIRTY)
            number = number // 2
        self.InitialDirtyAmount = self.CountDirty()
        return

    def SetWallsFromBinary(self,bin):
        self.NumCollisions = 0
        self.NumTurns = 0
        number = bin
        binDigits = self.Width * self.Height
        for b in range(0,binDigits):
            if (number%2 != 0):
                self.SetTileByNumber(b,WALL)
            number = number // 2
        self.InitialDirtyAmount = self.CountDirty()
        return

    def Collide(self,x=0,y=0):
        self.NumTurns += 1
        #assert self.NumTurns > (self.Width * self.Height * 4)
        #print("Turns: {}".format(self.NumTurns))
        if self.GetTile(x,y) == WALL:
            self.NumCollisions += 1
            return True
        else:
            return False

    def CountDirty(self):
        numDirty = 0
        for x in range(self.Width):
            for y in range(self.Height):
                if self.GetTile(x,y) == DIRTY:
                    numDirty += 1
        return numDirty

    def GetTileState(self, tile):
        if self.Grid[tile[0]][tile[1]] == DIRTY:
            return DIRTY
        else:
            return CLEAN

    def GetPercentClean(self):
        assert self.CountDirty() <= self.InitialDirtyAmount
        if self.InitialDirtyAmount <= 0:
            return 100
        return (1-(self.CountDirty()/self.InitialDirtyAmount)) * 100

    def RandomizeWithoutWalls(self):
        #assert False
        for x in range(self.Width):
            for y in range(self.Height):
                self.SetTile(x=x,y=y,val=random.randint(CLEAN,DIRTY))
        self.InitialDirtyAmount = self.CountDirty()
        if self.InitialDirtyAmount == 0:
            self.RandomizeWithoutWalls()

    def RandomizeWithWalls(self):
        #assert False
        for x in range(self.Width):
            for y in range(self.Height):
                self.SetTile(x,y,random.randint(CLEAN,WALL))
        self.InitialDirtyAmount = self.CountDirty()
        if self.InitialDirtyAmount == 0:
            self.RandomizeWithWalls()

    def GetPerformanceMeasure(self):
        perfmeasure = {"collisions":self.NumCollisions,"numTurns":self.NumTurns,"percentClean":self.GetPercentClean(),"score":((self.GetPercentClean() * CLEAN_WEIGHT) - (max(self.NumTurns,1)* STEPS_WEIGHT))}
        return perfmeasure

    def Visualize(self):
        print("visualizing w:{}, h:{}".format(self.Width,self.Height))
        for y in range (self.Height):
            for x in range (self.Width):
                print("[{}] ".format(self.GetTile(x,y)),end="")
            print("")
        perf = self.GetPerformanceMeasure()
        print("Collisions: {}, Steps: {}, Percent Cleaned: {}% Score: {}".format(perf['collisions'],perf['numTurns'],perf['percentClean'],perf['score']))
        return
