from turtle import circle, xcor
from CircleHolding import CircleHolding
from CenterHoldingPoint  import CenterHoldingPoint
import math
import copy

from Runway import Runway
class AirTrafficControl:
    def __init__(self,numRunway, heightR, widthR):
        self.numRunway = numRunway
        self.heightR = heightR
        self.widthR = widthR
        self.planeInAirSpace = []
        self.planesQ=[]
        self.runways=[]
        self.atcZone =10000
        self.circleHolding =[]
        self.holdPointList=[]
        self.runWaySizeCircleRadius =0
        self.minDistanceBetweenPlanes =100
        self.radiusCircleHoldZone=0
        self.distBetweenHoldPoints = 400
        self.firstNewX = 0 #store x coordinate of first point of Circle holding Point
        self.firstNewY= 0
       
        self.runWayNumber = -1
        for i in range(numRunway):
            self.runways.append(Runway())
    def goForLanding(self,indexOfPlane):
        runWayEnterance = [0,-350] 
        for x in range(len(self.runways)):
            if(self.runways[x].checkEmpty()):                
                runWayNumber = x
                self.runways[x].occupied()
                return runWayEnterance        
        return self.getEmptyCHPoint(indexOfPlane)
    def getEmptyCHPoint(self,position):
        
        return self.holdPointList[position-self.numRunway].getPosition()

    def checkWithin100():
        print("checking")
    def genCircleHolding(self): #this function will generate circles where holdings happen
        runWayEnterance = [0,-350] 
        radius= self.atcZone - self.minDistanceBetweenPlanes - self.runWaySizeCircleRadius # radius of circle where circle holding the holding points can be
        numZone = radius//self.distBetweenHoldPoints

        for x in range(int(numZone)):
            radiusCircleHolding = self.runWaySizeCircleRadius + 400*(x+1)
            self.circleHolding.append(CircleHolding(radiusCircleHolding)) # create appropriate num of circle holding
            numPoints = (2*self.circleHolding[x].getRadius()*3.14)//(400+500) # number of holding points
            for y in range(int(numPoints)):
                if(y==0):
                    if(x==0): ##checks for very first point only
                        self.holdPointList.append(CenterHoldingPoint(runWayEnterance[0],(runWayEnterance[1]-self.distBetweenHoldPoints),True))
                        self.firstNewX = runWayEnterance[0]
                        self.firstNewY = runWayEnterance[1]-self.distBetweenHoldPoints
                        angle = self.findOldAngle([self.firstNewX,self.firstNewY])                      
                        
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
                                                  
                else: # not the first point, populate centerholding w points
                    
                    angleBetweenEachPoint = (2*math.pi)/numPoints
                    prevHoldPoint = self.holdPointList[-1].getPosition()
                    angle = angle - angleBetweenEachPoint
                    newX =  radiusCircleHolding*math.cos(angle)
                    newY =  radiusCircleHolding*math.sin(angle)
                    self.holdPointList.append(CenterHoldingPoint(newX,newY,False))
           
            for x in range(len(self.holdPointList)):
                print(self.holdPointList[x].getPosition())

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
    def checkRunway(self):
        for x in range(len(self.runways)):
            if(self.runways[x].checkEmpty()):                
                runWayNumber = x
                self.runways[x].occupied()
                return True
        return False
    def updatePlanePos(self):
        runWayEnterance = [0,-350] 
        shiftCHPoint = False
        runWayNumber = -1
        planesLanded =[]

        for x in range(len(self.planeInAirSpace)) :
            
            if(self.planeInAirSpace[x].getLandingOrHolding()==""): #means plane was just created
                
                posDestination =[]
                print(" before")
                posDestination = self.goForLanding(x)
                print("plane " +str(x)+" :"+ str(posDestination))
                if(posDestination == runWayEnterance):
                    runWayNumber = self.runWayNumber             
                self.planeInAirSpace[x].angleToDestination(posDestination,runWayNumber) # get the destination coordinates (landing zone or holding point) and get the angle for it

            self.planeInAirSpace[x].updatePath()
            print("plane " +str(self.planeInAirSpace[x].getId())+" :"+ str(self.planeInAirSpace[x].returnPosition()))
            if(self.planeInAirSpace[x].getLandingOrHolding() == "Landing"):
                if(self.planeInAirSpace[x].endOfRunway()): # once plane are at the end of the runway
                    runWayNumber = self.planeInAirSpace[x].returnRunwayNumber()
                    self.runways[self.planeInAirSpace[x].returnRunwayNumber()].free()
                    # planesLanded.append(x)
                    shiftCHPoint = True
                    print("***************************************************************************************")
            if(self.planeInAirSpace[x].getLandingOrHolding() == "Holding"):
                if(self.checkRunway() and shiftCHPoint ==True):
                    print("Shifting")
                    self.planeInAirSpace[x].setDestination("Landing")
                    self.planeInAirSpace[x].angleToDestination(runWayEnterance,self.runWayNumber) # shift the destination for the first plane in q to runway enterance
                elif(shiftCHPoint == True):
                    self.planeInAirSpace[x].angleToDestination(self.getEmptyCHPoint(x-1),-1)
                    print("New holding point" + str(self.planeInAirSpace[x].returnPosition()))
        if(shiftCHPoint == True):
            self.planeInAirSpace.pop(0)

        

        



