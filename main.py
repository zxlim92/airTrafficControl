from AirTrafficControl import AirTrafficControl
from Plane import Plane
import math
import time

def main():
    planes = [] # store incoming planes
    frequency = 10
    airTrafficControl =  AirTrafficControl(2,500,100)
    airTrafficControl.genRunWaySize() # gen run way circle
    airTrafficControl.genCircleHolding() #gen holding circle and points
    
    a = Plane([0,-2000])
    a.angleToDestination([0,-350])
    b = Plane([0,-2000])
    b.angleToDestination([0,-350])
    c = Plane([0,-2000])
    c.angleToDestination([0,-350])
    airTrafficControl.addPlane(a)
    airTrafficControl.addPlane(b)
    airTrafficControl.addPlane(c)
    while (1):
        startTime = time.time()
        airTrafficControl.updatePlanePos() #update positons of plane     
        time.sleep((1/frequency) - ((time.time() - startTime) % 60.0))
        

if __name__ == "__main__":

    main()