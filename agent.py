from directions import *
from states import *
from actions import *

class Agent:
    Status = CLEAN
    FacingTile = CLEAN

    Position = (0,0)
    DirFacingVec = NORTH
    Environ = None

    def __init__(self, startingPos, startingDir, environ):
        self.Position = startingPos
        self.DirFacingVec = startingDir
        self.Environ = environ

    def GetPercept(self):
        self.Status = self.Environ.GetTile(x=self.Position[0],y=self.Position[1])
        self.FacingTile = self.Environ.GetTile(self.Position[0] + self.DirFacingVec[0],self.Position[1] + self.DirFacingVec[1])

    def Rotate(self, dir):
        self.DirFacingVec = RotateDirVec45Deg(self.DirFacingVec,dir)

        if print_rotations:
            if dir == CW:
                print("agent rotated 45 degrees clockwise")
            elif dir == CCW:
                print("agent rotated 45 degrees counterclockwise")
            print("agent direction: x:{} y:{}".format(self.DirFacingVec[0],self.DirFacingVec[1]))

    def MoveForward(self):
        newX = self.Position[0] + self.DirFacingVec[0]
        newY = self.Position[1] + self.DirFacingVec[1]
        if not self.Environ.Collide((newX,newY)):
            self.Position = (self.Position[0] + self.DirFacingVec[0],self.Position[1] + self.DirFacingVec[1])
            print("agent position: x:{} y:{}".format(self.Position[0],self.Position[1]))
            return True
        else:
            print("agent collided")
            return False

    def CleanTile(self):
        self.Environ.SetTile(self.Position[0],self.Position[1],CLEAN)
        return

    def Run(self):
        return
