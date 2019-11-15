import random

from states import *
from environment import *

class SmallChildren(Environment):
    def __init__(self,width,height):
        self.Width = width
        self.Height = height
        self.Grid = []
        for x in range(width):
            newCol = []
            for y in range(height):
                newCol.append(CLEAN)
            self.Grid.append(newCol)

    def GetPercentClean(self):
        if self.InitialDirtyAmount <= 0:
            return 100
        return (1-(self.CountDirty()/self.InitialDirtyAmount)) * 100

    def Collide(self,x=0,y=0):
        self.NumTurns += 1
        footstep = False
        for x in range(self.Width):
            for y in range(self.Height):
                if self.GetTile(x,y) == CLEAN:
                    footstep = random.randint(1,10) == 1
                    if footstep:
                        self.SetTile(x,y,DIRTY)

        #assert self.NumTurns > (self.Width * self.Height * 4)
        #print("Turns: {}".format(self.NumTurns))
        if self.GetTile(x,y) == WALL:
            self.NumCollisions += 1
            return True
        else:
            return False

    
