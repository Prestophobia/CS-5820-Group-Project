import sys
from math import sqrt
from math import pow
from math import degrees
from math import atan

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
        self.Log.append("finding all dirty tiles")
        for x in range(self.Environ.Width):
            for y in range(self.Environ.Height):
                if self.Environ.GetTileState((x,y)) == DIRTY:
                    self.DirtyTiles.append((x,y))

    def PrintDirtyTiles(self):
        self.Log.append("printing dirty tiles")
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
        self.Log.append("ClosestDirtyTile=" + str(closestTile))
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
        if target == None:
            return self.Position
        currentX = self.Position[0]
        currentY = self.Position[1]
        targetX = target[0]
        targetY = target[1]

        return ((targetX - currentX),(targetY - currentY))

    def GetDirection(self, current, target):
        # print("Current:" + str(current))
        # print("Target:" + str(target))
        if current != target:
            if current[0] == target[0]:
                if current[1] > target[1]:
                    direction = NORTH
                else:
                    direction = SOUTH
            elif current[1] == target[1]:
                if current[0] > target[0]:
                    direction = EAST
                else:
                    direction = WEST
            elif current[0] > target[0]: # east
                if current[1] > target[1]:
                    direction = NORTHEAST
                else:
                    direction = SOUTHEAST
            elif current[0] < target[0]: # west
                if current[1] > target[1]:
                    direction = NORTHWEST
                else:
                    direction = SOUTHWEST
            elif current[1] > target[1]: # south
                if current[0] > target[0]:
                    direction = SOUTHEAST
                else:
                    direction = SOUTHWEST
            elif current[1] < target [1]: # north
                if current[0] > target[0]:
                    direction = NORTHEAST
                else:
                    direction = NORTHWEST
            else:
                direction = WEST
        else:
            direction = WEST

        return direction

    def MoveTo(self, target):
        if target == None:
            return

        while self.Position != target:
            self.RotateUntil(self.GetDirection(self.Position, target))
            self.MoveForward()
        return

    def Run(self):
        while self.Environ.CountDirty() > 0:
            self.Log.append("DirtyCount=" + str(self.Environ.CountDirty()))
            self.GetPercept()
            if self.Status == DIRTY:
                self.CleanTile()
                self.RemoveFromKnownDirtyTiles(self.Position)

            self.MoveTo(self.GetClosestDirtyTile())
        return
