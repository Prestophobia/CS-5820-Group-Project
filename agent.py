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
        self.FacingTile = self.Environ.GetTile(self.Position[0] + self.DirFacingVec[0],self.Position[1] + self.DirFacingVec[1])

    def Rotate(self, dir):
        self.DirFacingVec = RotateDirVec45Deg(self.DirFacingVec,dir)
        if dir == CW:
            self.Log.append("agent rotated 45 degrees clockwise")
        elif dir == CCW:
            self.Log.append("agent rotated 45 degrees counterclockwise")
        self.Log.append("agent direction: x:{} y:{}".format(self.DirFacingVec[0],self.DirFacingVec[1]))
           

    def MoveForward(self):
        newX = self.Position[0] + self.DirFacingVec[0]
        newY = self.Position[1] + self.DirFacingVec[1]
        if not self.Environ.Collide((newX,newY)):
            self.Position = (self.Position[0] + self.DirFacingVec[0],self.Position[1] + self.DirFacingVec[1])
            self.Log.append("agent position: x:{} y:{}".format(self.Position[0],self.Position[1]))
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

        for i in range(n):
            self.Run()
            results = self.Environ.GetPerformanceMeasure()
            #print(results)
            cleanTotal += results['percentClean']
            assert results['percentClean']>=0
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
            assert results['score']>=0
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
        if numVariations > 10000:#prevent program from chugging by approximating
            return self.RunNTimes(10000)
        
        for b in range(numVariations):
            #print("binaryNumber: {}".format(b))
            self.Reset()
            self.Environ.SetGridFromBinary(b)
            self.Run()
            results = self.Environ.GetPerformanceMeasure()
            #print(results)
            cleanTotal += results['percentClean']
            assert results['percentClean']>=0
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
            assert results['score']>=0
            if results['score'] > scoreMax:
                scoreMax = results['score']
            if results['score'] < scoreMin:
                scoreMin = results['score']

        cleanAverage = cleanTotal/numVariations
        stepsAverage = stepsTotal/numVariations
        scoreAverage = scoreTotal/numVariations
        return {"cleanAvg":cleanAverage,"cleanMax":cleanMax,"cleanMin":cleanMin,"stepsAvg":stepsAverage,"stepsMax":stepsMax,"stepsMin":stepsMin,"scoreAvg":scoreAverage,"scoreMax":scoreMax,"scoreMin":scoreMin}



    def PrintLog(self):
        for entry in self.Log:
            print(entry)