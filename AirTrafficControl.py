from turtle import circle
from CircleHolding import CircleHolding
class AirTrafficControl:
    numRunway =0
    heightR =0
    widthR =0
    planes = []
    planesQ=[]
    runways=[]
    atcZone =10000
    circleHolding =[]
    runWaySize =0
    minDistanceBetweenPlanes =100
    radiusCircleHoldZone=0
    distBetweenPoints = 400
    def __init__(self,numRunway, heightR, widthR):
        self.numRunway = numRunway
        self.heightR = heightR
        self.widthR = widthR
    def goForLanding(plane):
        print("landing")
    def checkWithin100():
        print("checking")
    def genCircleHolding(self): #this function will generate circles where holdings happen
        radius= self.atcZone - self.minDistanceBetweenPlanes - self.runWaySize
        numZone = radius//self.distBetweenPoints
        for x in range(int(numZone)):
            self.circleHolding.append(CircleHolding(self.runWaySize + 400*(x+1))) # create appropriate num of circle holding
    def genRunWaySize(self):
        self.runWaySize = ((max(self.heightR,self.widthR))/2)+self.minDistanceBetweenPlanes
        



