from directions import *
from states import *
from agent import *

class RandomAgent(Agent):
    def __init__(self, startingPos, startingDir, environ):
        super().__init__(startingPos, startingDir, environ)
        self.AgentTypeName = "Random Reflex Agent"

    def Run(self):
        maxSteps = 100
        running = True
        if self.PrintMovements:
            print("agent starting position: x:{} y:{}".format(self.Position[0],self.Position[1]))
            print("agent starting direction: x:{} y:{}".format(self.DirFacingVec[0],self.DirFacingVec[1]))
        for step in range(maxSteps):
            self.CleanTile()
            r = random.randint(0,7)
            for rotations in range(r):
                self.Rotate(CW)
            self.MoveForward()
        return
