from directions import *
from states import *
from agent import *

class SimpleReflexAgent(Agent):
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

            if self.Status == DIRTY:
                self.CleanTile()

            if self.FacingTile == DIRTY:
                self.MoveForward()
            else:
                self.Rotate(CW) #45 deg

                self.GetPercept()
                if self.FacingTile == DIRTY:
                    self.MoveForward()
                else:
                    self.Rotate(CW) #90 deg
                    self.GetPercept()
                    if self.FacingTile == DIRTY:
                        self.MoveForward()
                    else:
                        self.Rotate(CW) #135 deg
                        self.GetPercept()
                        if self.FacingTile == DIRTY:
                            self.MoveForward()
                        else:
                            self.Rotate(CW) #180 deg
                            self.GetPercept()
                            if self.FacingTile == DIRTY:
                                self.MoveForward()
                            else:
                                self.Rotate(CW) #225 deg
                                self.GetPercept()
                                if self.FacingTile == DIRTY:
                                    self.MoveForward()
                                else:
                                    self.Rotate(CW) #270 deg
                                    self.GetPercept()
                                    if self.FacingTile == DIRTY:
                                        self.MoveForward()
                                    else:
                                        self.Rotate(CW) #315 deg
                                        self.GetPercept()
                                        if self.FacingTile == DIRTY:
                                            self.MoveForward()
                                        else:
                                            running = False

        return
