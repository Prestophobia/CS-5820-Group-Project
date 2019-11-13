import sys
from math import sqrt
from math import pow

from directions import *
from states import *
from agent import *

class SimpleReflexAgentWithEntireState(Agent):

    DirtyTiles = [] # Part of the state chosen is the agent knows all the dirty tiles
    targetPosition = None

    def __init__(self, startingPos, startingDir, environ):
        super().__init__(startingPos, startingDir, environ)
        self.AgentTypeName = "Simple Reflex Agent with entire State"
        self.GetDirtyTiles()

    def GetDirtyTiles(self):
        print("finding all dirty tiles")
        for x in range(self.Environ.Width):
            for y in range(self.Environ.Height):
                if self.Environ.GetTileState((x,y)) == DIRTY:
                    self.DirtyTiles.append((x,y))

    def PrintDirtyTiles(self):
        print("printing dirty tiles")
        print(len(self.DirtyTiles))
        for tile in self.DirtyTiles:
            print(tile)

    def GetClosestDirtyTile(self):
        closestTile = None
        closestDistance = sys.maxsize
        for tile in self.DirtyTiles:
            tempDistance = self.CalculateDistanceFromCurrent(tile)
            if closestDistance >= tempDistance:
                closestDistance = tempDistance
                closestTile = tile
        return closestTile

    def RemoveFromKnownDirtyTiles(self, toRemove):
        for tile in self.DirtyTiles:
            if tile == toRemove:
                self.DirtyTiles.remove(tile)
                return

    def CalculateDistanceFromCurrent(self, target):
        currentX = self.Position[0]
        currentY = self.Position[1]
        targetX = target[0]
        targetY = target[1]

        # distance between two 2-d points formula
        return sqrt(pow((currentX - targetX),2) + pow((currentY - targetY),2))

    def GetPathTo(self, target):
        currentX = self.Position[0]
        currentY = self.Position[1]
        targetX = target[0]
        targetY = target[1]

        return ((targetX - currentX),(targetY - currentY))

    def MoveTo(self, target):
        print(target)
        path = self.GetPathTo(target)
        # while self.Position != target:
        if path[0] > 0:
            # then we need to move west
            self.RotateUntil(WEST)
        elif path[0] < 0:
            # then we need to move east
            self.RotateUntil(EAST)
        while self.Position[0] != target[0]: # if no change on x, we don't need to move east or west
            print(str(self.Position[0]) + "," + str(target[0]))
            self.MoveForward()

        if path[1] > 0:
            # then we need to move north
            self.RotateUntil(NORTH)
        elif path[1] < 0:
            # then we need to move south
            self.RotateUntil(SOUTH)

        while self.Position[1] != target[1]: # if no change on y, we don't need to move north or south
            self.MoveForward()
        return

    def Run(self):
        while self.Environ.CountDirty() > 0:
            self.GetPercept()
            if self.Status == DIRTY:
                self.CleanTile()
                self.RemoveFromKnownDirtyTiles(self.Position)

            self.MoveTo(self.GetClosestDirtyTile())
        return
