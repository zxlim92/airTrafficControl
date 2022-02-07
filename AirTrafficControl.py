from turtle import circle
from CircleHolding import CircleHolding
from CenterHoldingPoint  import CenterHoldingPoint
import math
class AirTrafficControl:
    numRunway =0
    heightR =0
    widthR =0
    planeInAirSpace = []
    planesQ=[]
    runways=[]
    atcZone =10000
    circleHolding =[]
    holdPointList=[]
    runWaySizeCircleRadius =0
    minDistanceBetweenPlanes =100
    radiusCircleHoldZone=0
    distBetweenHoldPoints = 400
    runWayEnterance =(0,0) # position where plane can enter
    firstNewX = 0 #store x coordinate of first point of Circle holding Point
    firstNewY= 0
    runWayEnterance = [0,350]  
    def __init__(self,numRunway, heightR, widthR):
        self.numRunway = numRunway
        self.heightR = heightR
        self.widthR = widthR
    def goForLanding(self,plane):
        for x in range(len(self.runway)):
            if(self.runways[x].checkEmpty()):
                self.runways[x].planeLanding(plane)
                return self.runWayEnterance
        else:
            return(self.checkEmptyHoldingCircle())
    def checkEmptyHoldingCircle(self):
        for x in range (len(self.circleHolding)):
            if(CircleHolding[x].checkEmpty()):               
                return CircleHolding[x].getPosition()

    def checkWithin100():
        print("checking")
    def genCircleHolding(self): #this function will generate circles where holdings happen
        radius= self.atcZone - self.minDistanceBetweenPlanes - self.runWaySizeCircleRadius # radius of circle where circle holding the holding points can be
        numZone = radius//self.distBetweenHoldPoints
        for x in range(int(numZone)):


            radiusCircleHolding = self.runWaySizeCircleRadius + 400*(x+1)
            self.circleHolding.append(CircleHolding(radiusCircleHolding)) # create appropriate num of circle holding

            numPoints = (2*self.circleHolding[x].getRadius()*3.14)//(400+500) # number of holding points
            print(" num points : "+ str(numPoints))
            print(" size radius "+str(radiusCircleHolding))
            
            for y in range(int(numPoints)):
                
                if(y==0):
                    if(x==0): ##checks for very first point only
                        self.holdPointList.append(CenterHoldingPoint(self.runWayEnterance[0],(self.runWayEnterance[1]-self.distBetweenHoldPoints-self.runWaySizeCircleRadius),True))
                        self.firstNewX = self.runWayEnterance[0]
                        self.firstNewY = self.runWayEnterance[1]-self.distBetweenHoldPoints-self.runWaySizeCircleRadius
                        print("FORST  + " + str(self.firstNewX)+ " "+str( self.firstNewY))
                        angle = self.findOldAngle([self.firstNewX,self.firstNewY])
                        print("origin angle " + str(angle))
                    else:
                        prevHoldPoint = self.holdPointList[0].getPosition()
                        if(prevHoldPoint[0]!=0):
                            angle = math.tan(prevHoldPoint[1]/prevHoldPoint[0])
                        elif(prevHoldPoint[1]<0):
                            angle = - math.pi/2
                            
                        else:
                            angle = math.pi/2
                        self.firstNewX = round(radiusCircleHolding *math.cos(angle),3)
                        self.firstNewY= round(radiusCircleHolding * math.sin(angle),3)
                        self.holdPointList.append(CenterHoldingPoint(self.firstNewX,self.firstNewY,True))                    
                        print("first " + str(self.firstNewX)+" , "+ str(self.firstNewY))                    
                else: # not the first point, populate centerholding w points
                    print("----------------")
                    # print("first :" +str(self.holdPointList[-1].getPosition()))
                    # print("length" + str(len(self.holdPointList)-1))
                    
                    angleBetweenEachPoint = (2*math.pi)/numPoints
                    # chordDistance = 2*radiusCircleHolding*math.sin(angleBetweenEachPoint/2)
                    prevHoldPoint = self.holdPointList[-1].getPosition()
                    # oldAngle = self.findOldAngle([prevHoldPoint[0],prevHoldPoint[1]])
                    
                    angle = angle - angleBetweenEachPoint
                    print(  "ANGLE" + str(angle))
                    newX =  radiusCircleHolding*math.cos(angle)
                    newY =  radiusCircleHolding*math.sin(angle)
              
                    print("new points "+str(newX)+" , "+ str(newY))
                    self.holdPointList.append(CenterHoldingPoint(newX,newY,True))

    def findOldAngle(self,prevHoldPoint):
        
        if(prevHoldPoint[0]!=0):
            angle = math.tan(prevHoldPoint[1]/prevHoldPoint[0])
        elif(prevHoldPoint[1]<0):
            angle = 3 * math.pi/2                        
        elif(prevHoldPoint[1]>0):
            angle = math.pi/2
        else:
            angle =0
        return angle
        
    def genRunWaySize(self):
        self.runWaySizeCircleRadius = ((max(self.heightR,self.widthR*self.numRunway))/2)+self.minDistanceBetweenPlanes

    def addPlane(self, plane):
        self.planeInAirSpace.append(plane)
        
    def updatePlanePos(self):
        
        planesLanded =[]
        for x in range(len(self.planeInAirSpace)) :
            print(x)
            if(self.planeInAirSpace[x].getLandingOrHolding()==""): #means plane was just created
                self.planeInAirSpace[x].angleToDestination(self.goForLanding(self.planeInAirSpace[x])) # get the destination coordinates (landing zone or holding point) and get the angle for it
            self.planeInAirSpace[x].updatePath()
            if(self.planeInAirSpace[x].getLandingOrHolding() == "Landing"):
                if(self.planeInAirSpace[x].endOfRunway()):
                    
                    planesLanded.append(x)
                    
                    print("Last plane " + str(self.planeInAirSpace[0].getLandingOrHolding()) )
        for i in range(len(planesLanded)): #assuming 2 planes can land at the same time
            print("plane gone")
            self.planeInAirSpace.pop()
            planesLanded.pop()
        

        



