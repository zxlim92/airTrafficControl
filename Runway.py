class Runway:
    __plane = None
    
    def getPlaneRunway(self):
        return self.__plane
    def checkEmpty(self):
        if(self.__plane is None):
            return True
        return False
    