from directions import *
from states import *
from agent import *

IDLE = 0
MOVING = 1
TURNING = 2
TERMINATING = 3
CLEANING = 4

class StateBot2(Agent):
    #state
    State = IDLE

    Battery = 100

    def __init__(self, startingPos, startingDir, environ):
        super().__init__(startingPos, startingDir, environ)
        self.AgentTypeName = "Simple Reflex Agent"

    def Run(self):
        running = True
        if self.PrintMovements:
            print("agent starting position: x:{} y:{}".format(self.Position[0],self.Position[1]))
            print("agent starting direction: x:{} y:{}".format(self.DirFacingVec[0],self.DirFacingVec[1]))
        while running:
            
            self.GetPercept()
            
            if self.State == IDLE:
                self.Log.append("State: IDLE")
                if self.Status == DIRTY:
                    self.State = CLEANING
                else:
                    self.State = MOVING

            elif self.State == CLEANING:
                self.Log.append("State: CLEANING")
                self.CleanTile()
                self.State = MOVING
                
            elif self.State == MOVING:
                self.Log.append("State: MOVING")
                self.Battery -= 1
                self.MoveForward()
                self.GetPercept()
                if self.Status == DIRTY:
                    self.State = CLEANING
                elif self.FacingTile == WALL:
                    self.State = TURNING
            
            elif self.State == TURNING:
                self.Log.append("State: TURNING")
                self.Rotate(CCW)
                self.GetPercept()
                for r in range(8):
                    self.Rotate(CCW)
                    self.GetPercept()
                    if self.FacingTile == DIRTY:
                        self.State = MOVING
                        break
                if self.FacingTile < WALL:
                    self.State = MOVING

            
            if self.Battery <= 0:
                running = False

            if self.Environ.CountDirty() <= 0:
                running = False


        return
