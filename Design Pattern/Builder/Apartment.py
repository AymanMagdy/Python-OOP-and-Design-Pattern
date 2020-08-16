class Apartment:
    def __init__(self):
        self.__doors = None
        self.__gardenSize = None
        self.__heatingType = None
        self.__heatingPower = None

    def setDoors(self, doors):
        self.__doors = doors
    
    def setGarden(self, gardenSize):
        self.__gardenSize = gardenSize
    
    def setHeating(self, heatingType, heatingPower):
        self.__heatingType = heatingType
        self.__heatingPower = heatingPower

    def getDoors(self):
        return self.__doors
    
    def getGarden(self):
        return self.__gardenSize
    
    def getHeating(self):
        heating = {
            "Heating type": self.__heatingType,
            "Heating power": self.__heatingPower
        }

        return heating

    def getSwimmingPool(self):
        return self.__swimmmingPool
    
    def getGarage(self):
        return self.__garage