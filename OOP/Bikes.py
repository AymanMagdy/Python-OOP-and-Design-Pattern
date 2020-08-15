import json
from Vehicles import Vehicles

class Bikes(Vehicles):

    vehicleType = "Bikes"
    bikeModel = ""
    bikeType = ""
    bikeYear = 0

    # The constructor with intializing all the class bikes variables.

    def __init__(self, bikeModel, bikeType, bikeYear):
        Vehicles.setVehicleType(self, self.vehicleType)
        self.bikeModel = bikeModel
        self.bikeType = bikeType
        self.bikeYear = bikeYear
    
    def numberOfDoors(self):
        return False

    # The Get methods for all the class variables

    def getVehicleType(self):
        if self.vehicleType == "":
            return False
        else:
            return self.vehicleType
    
    def getBikeModel(slef):
        if self.bikeModel == "":
            return False
        else:
            return self.bikeModel
    
    def getBikeType(self):
        if self.bikeType == "":
            return False
        else:
            return self.bikeType
    
    def getBikeYear(self):
        if self.bikeYear == 0:
            return False
        else:
            return self.bikeYear
    
    def getBike(self):
        bikeJsn = {
            "Vehilcle Type": Vehicles.getVehicleType(self),
            "Bike type": self.bikeType,
            "Bike model": self.bikeModel,
            "Bike year": self.bikeYear,
            "Number of doors:": self.numberOfDoors()
        }

        return json.dumps(bikeJsn)

class PedalBikes(Bikes):
    def __init__(self, bikeModel, bikeYear):
        bikeType = "Pedal Bike"
        super().__init__(bikeModel, bikeType, bikeYear)

class PedalBikes(Bikes):
    def __init__(self, bikeModel, bikeYear):
        bikeType = "Pedal Bike"
        super().__init__(bikeModel, bikeType, bikeYear)