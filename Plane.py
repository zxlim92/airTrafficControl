import math

from Runway import Runway
class Plane:

    
    def __init__(self,position,id):
        self.__id = id
        self.__position = position
        self.__centerPointHC = [0,0]
        self.__angle =0
        self.__speed = 140 
        self.__frequency =10
        self.__runwayLength = 500
        self.__posDestination = [0,0]
        self.__landed = False
        self.__endOfRunway = False
        self.__LandingOrHolding ="" # should store what the plane is doing, eg Landing or Holding
        self.__runwayPos = [0,-350]
        self.__arrivedAtHoldingZone = False
        self.__runwayNumber =-1
    def getId(self):
        return self.__id
    def returnPosition(self):
        return self.__position
    def setPosition(self, newPos):
        self.__position = newPos
    def flyTowardsCH(self,centerPoint):
        print() # find angle  , centerpoint will be destination7
    def angleToDestination(self,posDestination,runwayNumber):
        # print("here " + str(posDestination))
        self.__posDestination = posDestination
        print(" desintion plz " + str(posDestination))
        if(posDestination == self.__runwayPos):
            self.__LandingOrHolding = "Landing"
            print("Going for Landingggggggggggggggggggg + " + str(self.__position))
            self.__runwayNumber = runwayNumber
        else:
            self.__LandingOrHolding = "Holding"
            # print("goin to holding point")
        diffX = self.__position[0] - posDestination[0]
        diffY = self.__position[1] - posDestination[1]
        # print("x "+str(diffX))
        # print("y "+str(diffY))
        # self.__angle=math.tan(diffY/diffX)
        if(diffY!=0):
            self.__angle=math.tan(diffX/diffY)
   #         print("angle is:L " + str(self.__angle))
        elif(diffX<0):
            self.__angle = 3 * math.pi/2                        
        elif(diffX>0):
            self.__angle = math.pi/2
        else:
            self.__angle =0
        print("Angle : " + str(self.__angle))
        print("cuyrrrent position " + str(self.__position))
    def endOfRunway(self):
        return self.__endOfRunway
    def arrivedAtHz(self):
        return self.__arrivedAtHoldingZone
    def updatePath(self):
        #(self.__position[0] - self.__posRunway[0])**2 + (self.__position[0] - self.__posRunway[0])**2)**0.5
        distanceToDestination = (((self.__position[1] - self.__posDestination[1])**2)+((self.__position[0] - self.__posDestination[0])**2) )**0.5
        if((distanceToDestination<  (self.__speed/self.__frequency)) and self.__landed == False and self.__LandingOrHolding == "Holding"):

            
            self.__angle =0
            self.__position[0] =self.__posDestination[0]
            self.__position[1]= self.__posDestination[1]
            # self.__posDestination[0] = self.__runwayPos[0]
            # self.__posDestination[1] = self.__runwayPos[1] + self.__runwayLength
            
        elif(self.__LandingOrHolding == "Landing" and (distanceToDestination<  (self.__speed/self.__frequency)) and self.__landed == False): # just landed beigning of runway
            self.__landed = True
            self.__angle =0
            self.__position[0] =self.__posDestination[0]
            self.__position[1]= self.__posDestination[1]
            self.__posDestination[0] = self.__runwayPos[0]
            self.__posDestination[1] = self.__runwayPos[1] + self.__runwayLength
            print("arrived at runway")
        elif(self.__landed == True and self.__position[0] == float(0) and self.__position[1] >=float(self.__runwayPos[1] + self.__runwayLength)): #end of runway
            print("end of runway")
            self.__endOfRunway = True
        elif(self.__LandingOrHolding == "Holding" and (distanceToDestination<  (self.__speed/self.__frequency))):
            print("Arrived at holding point")
            print("my destination : " + str(self.__posDestination))
            print("current pos " + str(self.__position))
            print(self.__LandingOrHolding)
        else:
            # print("distance away " + str((((self.__position[1] - self.__posDestination[1])**2)+((self.__position[0] - self.__posDestination[0])**2) )**0.5))
            if(self.__position[0] >self.__posDestination[0]):
                self.__position[0] = -1* abs(math.sin(self.__angle) * self.__speed *(1/self.__frequency)) + self.__position[0]
                
            else:
                self.__position[0] =  abs(math.sin(self.__angle) * self.__speed *(1/self.__frequency))+ self.__position[0]
            if(self.__position[1] >self.__posDestination[1]):
                self.__position[1] = -1*abs(math.cos(self.__angle) * self.__speed *(1/self.__frequency)) + self.__position[1]
            else:
                self.__position[1] = abs(math.cos(self.__angle) * self.__speed *(1/self.__frequency)) + self.__position[1]
        # print(str(self.__position))
    def getLandingOrHolding(self):
        return self.__LandingOrHolding    
    def setDestination(self, destination):
        self.__LandingOrHolding = destination
    def returnRunwayNumber(self):
        return self.__runwayNumber
    