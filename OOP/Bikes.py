import json
from Vehicles import Vehicles

class Bikes(Vehicles):

    vehicleType = "Bikes"
    bikeModel = ""
    bikeType = ""
    bikeYear = 0

    # The constructor with intializing all the class bikes variables.

    def __init__(self, bikeModel, bikeType, bikeYear):
        Vehicles.vehicleType = self.vehicleType
        self.bikeModel = bikeModel
        self.bikeType = bikeType
        self.bikeYear = bikeYear

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
            "Bike type": self.bikeType,
            "Bike model": self.bikeModel,
            "Bike year": self.bikeYear
        }

        return json.dumps(bikeJsn)

class PedalBike(Bikes):
    def __init__(self, bikeModel, bikeYear):
        bikeType = "Pedal Bike"
        super().__init__(bikeModel, bikeType, bikeYear)

class MotorBike(Bikes):
    def __init__(self, bikeModel, bikeYear):
        bikeType = "Motor Bike"
        super().__init__(bikeModel, bikeType, bikeYear)

