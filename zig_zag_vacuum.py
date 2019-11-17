from directions import *
from states import *
from agent import *

class ZigZagVacuum(Agent):
    def __init__(self, startingPos, startingDir, environ):
        super().__init__(startingPos, startingDir, environ)
        self.AgentTypeName = "Zig Zag Agent"

    def Run(self):
        steps = 0
        running = True
        if self.PrintMovements:
            print("agent starting position: x:{} y:{}".format(self.Position[0],self.Position[1]))
            print("agent starting direction: x:{} y:{}".format(self.DirFacingVec[0],self.DirFacingVec[1]))
        while running and steps < 100:
            steps += 1
            self.GetPercept() # >
            if self.Status == DIRTY:
                self.CleanTile()
            if self.FacingTile == WALL: # >
                rotationDir = CCW
                if self.DirFacingVec == WEST:
                    rotationDir = CCW

                self.Rotate(rotationDir)
                self.Rotate(rotationDir) # V

                self.GetPercept()

                if self.FacingTile == WALL:
                    running = False

                else:
                    self.MoveForward()
                    self.Rotate(rotationDir)
                    self.Rotate(rotationDir) # <
            else:
                self.MoveForward()
            if self.Environ.CountDirty() <= 0:
                running = False
