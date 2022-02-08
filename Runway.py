class Runway:
    
    def __init__(self):
        self.__plane = None
        self.__empty = True
    # def getPlaneRunway(self):
    #     return self.__empty
    def checkEmpty(self):
        if(self.__empty):
            return True

        return False
    def planeLanding(self,plane):
        self.__empty = True

    def occupied(self):
        self.__empty = False
    def free(self):
        print("freed")
        self.__empty = True
    