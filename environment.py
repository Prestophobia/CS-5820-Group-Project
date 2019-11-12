import random

from states import *

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
        self.Grid[x][y] = val

    def Collide(self,pos):
        self.NumTurns += 1
        if pos[0] >= self.Width or pos[1] >= self.Height:
            self.NumCollisions += 1
            return True
        elif self.GetTile(pos[0],pos[1]) == WALL:
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

    def GetPercentClean(self):
        return (1-(self.CountDirty()/self.InitialDirtyAmount)) * 100

    def RandomizeWithoutWalls(self):
        for x in range(self.Width):
            for y in range(self.Height):
                self.SetTile(x,y,random.randint(CLEAN,DIRTY))
        self.InitialDirtyAmount = self.CountDirty()
        if self.InitialDirtyAmount == 0:
            self.RandomizeWithoutWalls()

    def RandomizeWithWalls(self):
        for x in range(self.Width):
            for y in range(self.Height):
                self.SetTile(x,y,random.randint(CLEAN,WALL))
        self.InitialDirtyAmount = self.CountDirty()
        if self.InitialDirtyAmount == 0:
            self.RandomizeWithWalls()

    
    def GetPerformanceMeasure(self):
        perfmeasure = {"collisions":self.NumCollisions,"numTurns":self.NumTurns,"percentClean":self.GetPercentClean()}
        return perfmeasure

    def Visualize(self):
        print("visualizing w:{}, h:{}".format(self.Width,self.Height))
        for y in range (self.Height):
            for x in range (self.Width):
                print("[{}] ".format(self.GetTile(x,y)),end="")
            print("")
        print("Collisions: {}, Steps: {}, Percent Cleaned: {}%".format(self.NumCollisions, self.NumTurns,self.GetPercentClean()))
        return
