import json
from Vehicles import Vehicles

class Cars(Vehicles):

    carType = ""
    carYear = ""
    carMotorType = ""
    carModelName = ""
    carNumberOfDoors = ""
    vehicleType = ""

# The set methods for the car class..

    def __init__(self, carType, carYear, carModelName, carMotorType, carNumberOfDoors):
        Vehicles.vehicleType = "Cars"
        self.carType = carType
        self.carYear = carYear
        self.carModelName = carModelName
        self.carMotorType = carMotorType
        self.carNumberOfDoors = carNumberOfDoors

# The get methods for the car class
    
    def getMotorType(self):
        if self.carMotorType == "":
            return False
        else:
            return self.carMotorType
    
    def getModelName(self):
        if self.carModelName == "":
            return False
        else:
            return self.carModelName
    
    def getCarYear(self):
        return self.year
    
    def getNumberOfDoors(self):
        if vehicleType == "Cars":
            numberOfDoors = vehicles.getNumberOfdoors()
            return numberOfDoors
    
    def getCar(self):
        carJsn = {
            "Car Type": self.carType,
            "Car Model": self.carModelName,
            "Car doors": self.carNumberOfDoors,
            "Car year": self.carYear
        }
        return json.dumps(carJsn)


class Pickups(Cars):
    def __init__(self, carYear, carModelName, carMotorType, carNumberOfDoors):
        carType = "pick-up"
        super().__init__(carType, carYear, carModelName, carMotorType, carNumberOfDoors)

class SportsCar(Cars):
    def __init__(self, carYear, carModelName, carMotorType, carNumberOfDoors):
        carType = "sports-car"
        super().__init__(carType, carYear, carModelName, carMotorType, carNumberOfDoors)

class EstateCars(Cars):
    def __init__(self, carYear, carModelName, carMotorType, carNumberOfDoors):
        carType = "Estate Cars"
        super().__init__(carType, carYear, carModelName, carMotorType, carNumberOfDoors)

car = Pickups(2015, "ip", "d", "2")
print(car.getCar())