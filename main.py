from AirTrafficControl import AirTrafficControl
from Plane import Plane
import math
import time
from random import random

def randomGenPlanes(id):
    angle = random()*2*math.pi
    x = math.cos(angle) * 10000
    y= math.sin(angle) * 10000
    return Plane([x,y],id)
def main():
    id =0 
    planes = [] # store incoming planes
    frequency = 10
    airTrafficControl =  AirTrafficControl(1,500,100)
    airTrafficControl.genRunWaySize() # gen run way circle
    airTrafficControl.genCircleHolding() #gen holding circle and points
    
  
    airTrafficControl.addPlane(randomGenPlanes(id))
    id = id +1
    while (1):
        if(random() < 0.01): # generate plane w a 1% chance every 0.1 seconds
            airTrafficControl.addPlane(randomGenPlanes(id))
            id = id +1
            print("New plane has been generated")
        startTime = time.time()
        airTrafficControl.updatePlanePos() #update positons of plane    
        
        time.sleep((1/frequency) - ((time.time() - startTime) % 60.0))

        

if __name__ == "__main__":

    main()