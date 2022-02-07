import math

from Runway import Runway
class Plane:
    __position = [0,0]
    __centerPointHC = [0,0]
    __angle =0
    __speed = 140 
    __frequency =10
    __runwayLength = 500
    __posDestination = [0,0]
    __landed = False
    __endOfRunway = False
    __LandingOrHolding ="" # should store what the plane is doing, eg Landing or Holding
    __runwayPos = [0,-350]
    __arrivedAtHoldingZone = False
    def __init__(self,position):
        print("plane")
        self.__position = position
    def returnPosition(self):
        return self.__position
    def setPosition(self, newPos):
        self.__position = newPos
    def flyTowardsCH(self,centerPoint):
        print() # find angle  , centerpoint will be destination7
    def angleToDestination(self,posDestination):
        self.__posDestination = posDestination
        if(posDestination == self.__runwayPos):
            self.__LandingOrHolding = "Landing"
            print("Going for Landing")
        else:
            self.__LandingOrHolding = "Holding"
            print("goin to holding circle")
        diffX = self.__position[0] - posDestination[0]
        diffY = self.__position[1] - posDestination[1]
        print("x "+str(diffX))
        print("y "+str(diffY))
        # self.__angle=math.tan(diffY/diffX)
        if(diffY!=0):
            self.__angle=math.tan(diffX/diffY)
            print("angle is:L " + str(self.__angle))
        elif(diffX<0):
            self.__angle = 3 * math.pi/2                        
        elif(diffX>0):
            self.__angle = math.pi/2
        else:
            self.__angle =0
        
    def endOfRunway(self):
        return self.__endOfRunway
        
    def updatePath(self):
        #(self.__position[0] - self.__posRunway[0])**2 + (self.__position[0] - self.__posRunway[0])**2)**0.5
        distanceToDestination = (((self.__position[1] - self.__posDestination[1])**2)+((self.__position[0] - self.__posDestination[0])**2) )**0.5
        if((distanceToDestination<  (self.__speed/self.__frequency)) and self.__landed == False):

            self.__landed = True
            self.__angle =0
            self.__position[0] =self.__posDestination[0]
            self.__position[1]= self.__posDestination[1]
        elif(self.__landed == True and self.__position[0] == float(0) and self.__position[1] >=float(self.__posDestination[1] +self.__runwayLength)):
            print("end of runway")
            self.__endOfRunway = True
        elif(self.__LandingOrHolding == "Holding" and (distanceToDestination<  (self.__speed/self.__frequency))):
            print("Arrived at holding point")
        else:
            print("distance away " + str((((self.__position[1] - self.__posDestination[1])**2)+((self.__position[0] - self.__posDestination[0])**2) )**0.5))
            self.__position[0] = math.sin(self.__angle) * self.__speed *(1/self.__frequency) + self.__position[0]
            self.__position[1] = math.cos(self.__angle) * self.__speed *(1/self.__frequency) + self.__position[1]
        print(str(self.__position))
    def getLandingOrHolding(self):
        return self.__LandingOrHolding    
    def setDestination(self, destination):
        self.__LandingOrHolding = destination

    