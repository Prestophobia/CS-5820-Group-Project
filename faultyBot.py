from directions import *
from states import *
from agent import *
from bumpBot import *
from murphyBot import *
import random

IDLE = 0
MOVING = 1
TURNING = 2
TERMINATING = 3
CLEANING = 4

class FaultyBot(MurphyBot):
    #state
    State = IDLE

    Battery = 100

    def __init__(self, startingPos, startingDir, environ):
        super().__init__(startingPos, startingDir, environ)
        self.AgentTypeName = "Faulty Murphy's law Agent"

    def GetPercept(self):
        self.Status = self.Environ.GetTile(x=self.Position[0],y=self.Position[1])
        unlucky = (random.randint(1,4) == 10)
        #assert self.Status == WALL #no wall climbing
        if self.Status == WALL:
            print("On wall")
            print("LOG")
            print("-------------------------------------------")
            self.PrintLog()
            print("-------------------------------------------")
        self.FacingTile = self.Environ.GetTile(self.Position[0] + self.DirFacingVec[0],self.Position[1] + self.DirFacingVec[1])
        if unlucky:
            if self.FacingTile == DIRTY:
                self.FacingTile = CLEAN
            elif self.FacingTile == CLEAN:
                self.FacingTile = DIRTY


