from directions import *
from states import *
from agent import *
from bumpBot import *
import random

IDLE = 0
MOVING = 1
TURNING = 2
TERMINATING = 3
CLEANING = 4

class MurphyBot(BumpBot):
    #state
    State = IDLE

    Battery = 100

    def __init__(self, startingPos, startingDir, environ):
        super().__init__(startingPos, startingDir, environ)
        self.AgentTypeName = "Murphy's law Agent"

    def CleanTile(self):
        self.GetPercept()
        unlucky = (random.randint(1,4) == 1)
        if unlucky:
            self.Environ.SetTile(self.Position[0],self.Position[1],DIRTY)
        else:
            self.Environ.SetTile(self.Position[0],self.Position[1],CLEAN)
        return


