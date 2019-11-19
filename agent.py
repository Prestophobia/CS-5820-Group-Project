from directions import *
from states import *
from actions import *
from environment import *

class Agent:
    AgentTypeName = "Blank Agent"
    Status = CLEAN
    FacingTile = CLEAN

    Position = (0,0)
    DirFacingVec = NORTH
    Environ = None

    StartingPos = (0,0)
    StartingDir = NORTH

    PrintMovements = False
    PrintCollisions = False

    Log = []

    def __init__(self, startingPos, startingDir, environ):
        self.StartingPos = startingPos
        self.Position = startingPos
        self.StartingDir = startingDir
        self.DirFacingVec = startingDir
        self.Environ = environ

    def Reset(self):
        self.Position = self.StartingPos
        self.DirFacingVec = self.StartingDir
        self.Log.clear()
        return self

    def GetPercept(self):
        self.Status = self.Environ.GetTile(x=self.Position[0],y=self.Position[1])
        #assert self.Status == WALL #no wall climbing
        if self.Status == WALL:
            print("On wall")
            print("LOG")
            print("-------------------------------------------")
            self.PrintLog()
            print("-------------------------------------------")
        self.FacingTile = self.Environ.GetTile(self.Position[0] + self.DirFacingVec[0],self.Position[1] + self.DirFacingVec[1])

    def Rotate(self, dir):
        self.DirFacingVec = RotateDirVec45Deg(self.DirFacingVec,dir)
        if dir == CW:
            self.Log.append("agent rotated 45 degrees clockwise")
        elif dir == CCW:
            self.Log.append("agent rotated 45 degrees counterclockwise")
        self.Log.append("agent direction: x:{} y:{}".format(self.DirFacingVec[0],self.DirFacingVec[1]))

    def RotateUntil(self, targetDirection):
        while self.DirFacingVec != targetDirection:
            self.Rotate(self.GetSmartRotationDirection(self.DirFacingVec, targetDirection))
        return

    def GetSmartRotationDirection(self, currentDirection, targetDirection):
        # add 45 degree if's
        if currentDirection == NORTH and targetDirection == WEST:
            return CCW
        if currentDirection == NORTHWEST and targetDirection == WEST:
            return CCW
        if currentDirection == WEST and targetDirection == SOUTH:
            return CCW
        if currentDirection == SOUTHWEST and targetDirection == SOUTH:
            return CCW
        if currentDirection == SOUTH and targetDirection == EAST:
            return CCW
        if currentDirection == SOUTHEAST and targetDirection == EAST:
            return CCW
        if currentDirection == EAST and targetDirection == NORTH:
            return CCW
        if currentDirection == NORTHEAST and targetDirection == NORTH:
            return CCW
        return CW

    def MoveForward(self):
        newX = self.Position[0] + self.DirFacingVec[0]
        newY = self.Position[1] + self.DirFacingVec[1]
        tileOccupied = self.Environ.Collide(newX,newY) or self.Environ.GetTile(newX,newY) == WALL
        if not tileOccupied:
            #assert self.Environ.GetTile(newX,newY) == WALL
            self.Position = (newX,newY)
            self.Log.append("agent position: x:{} y:{}".format(newX,newY))
            return True
        else:
            self.Log.append("agent collided")
            return False

    def CleanTile(self):
        self.Environ.SetTile(self.Position[0],self.Position[1],CLEAN)
        return

    def Run(self):
        return

    def RunNTimes(self,n):
        cleanTotal = 0
        cleanMax = 0
        cleanMin = 100

        stepsTotal = 0
        stepsMax = 0
        stepsMin = self.Environ.Width * self.Environ.Height * 3

        scoreTotal = 0
        scoreMax = 0
        scoreMin = cleanMin
        for x in range(self.Environ.Width):
            for y in range(self.Environ.Height):
                self.StartingPos = (x,y)
                for i in range(n):
                    self.Run()
                    results = self.Environ.GetPerformanceMeasure()
                    #print(results)
                    cleanTotal += results['percentClean']
                    #assert results['percentClean']>=0
                    if results['percentClean'] > cleanMax:
                        cleanMax = results['percentClean']
                    if results['percentClean'] < cleanMin:
                        cleanMin = results['percentClean']

                    stepsTotal += results['numTurns']
                    assert results['numTurns']>=0
                    if results['numTurns'] > stepsMax:
                        stepsMax = results['numTurns']
                    if results['numTurns'] < stepsMin:
                        stepsMin = results['numTurns']

                    scoreTotal += results['score']
                    #assert results['score']>=0
                    if results['score'] > scoreMax:
                        scoreMax = results['score']
                    if results['score'] < scoreMin:
                        scoreMin = results['score']

                    self.Reset()
                    self.Environ.Reset()
        cleanAverage = cleanTotal/n
        stepsAverage = stepsTotal/n
        scoreAverage = scoreTotal/n
        return {"cleanAvg":cleanAverage,"cleanMax":cleanMax,"cleanMin":cleanMin,"stepsAvg":stepsAverage,"stepsMax":stepsMax,"stepsMin":stepsMin,"scoreAvg":scoreAverage,"scoreMax":scoreMax,"scoreMin":scoreMin}

    def RunAllEnvironVariations(self):
        cleanTotal = 0
        cleanMax = 0
        cleanMin = 100

        stepsTotal = 0
        stepsMax = 0
        stepsMin = 100

        scoreTotal = 0
        scoreMax = 0
        scoreMin = cleanMin

        numVariations = 1<<(self.Environ.Width * self.Environ.Height)
        totalVariations = numVariations * (self.Environ.Width * self.Environ.Height)
        if numVariations > 10000:#prevent program from chugging by approximating
            return self.RunNTimes(10000)

        for x in range(self.Environ.Width):
            for y in range(self.Environ.Height):
                self.StartingPos = (x,y)
                for b in range(numVariations):
                    #print("binaryNumber: {}".format(b))
                    self.Reset()
                    self.Environ.SetGridFromBinary(b)
                    self.Run()
                    results = self.Environ.GetPerformanceMeasure()
                    #print(results)
                    cleanTotal += results['percentClean']
                    #assert results['percentClean']>=0
                    if results['percentClean'] > cleanMax:
                        cleanMax = results['percentClean']
                    if results['percentClean'] < cleanMin:
                        cleanMin = results['percentClean']

                    stepsTotal += results['numTurns']
                    #assert results['numTurns']>=0
                    if results['numTurns'] > stepsMax:
                        stepsMax = results['numTurns']
                    if results['numTurns'] < stepsMin:
                        stepsMin = results['numTurns']

                    scoreTotal += results['score']
                    #assert results['score']>=0
                    if results['score'] > scoreMax:
                        scoreMax = results['score']
                    if results['score'] < scoreMin:
                        scoreMin = results['score']



        cleanAverage = cleanTotal/totalVariations
        stepsAverage = stepsTotal/totalVariations
        scoreAverage = scoreTotal/totalVariations
        return {"cleanAvg":cleanAverage,"cleanMax":cleanMax,"cleanMin":cleanMin,"stepsAvg":stepsAverage,"stepsMax":stepsMax,"stepsMin":stepsMin,"scoreAvg":scoreAverage,"scoreMax":scoreMax,"scoreMin":scoreMin}



    def PrintLog(self):
        for entry in self.Log:
            print(entry)
