from Plane import Plane
class CenterHoldingPoint:
    __plane = None
    __position = [0,0]
    __firstPoint = False
    def __init__(self,xPos,yPos,firstPoint):
        self.__position[0] = xPos
        self.__position[1] = yPos
        self.__firstPoint = firstPoint
    def getPosition(self):
        return self.__position
    def isFirst(self):
        return self.__firstPoint