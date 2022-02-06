from AirTrafficControl import AirTrafficControl
import math
def main():
    airTrafficControl =  AirTrafficControl(2,500,100)
    airTrafficControl.genRunWaySize()
    airTrafficControl.genCircleHolding()

if __name__ == "__main__":

    main()