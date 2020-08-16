from Builder import Builder, Doors, Garage, Heating, SwimmingPool

class PalaceBuilder(Builder):
    def getDoors(self):
        doors = Doors()
        doors.numberOfDoors = 15

        return doors

    def getGarden(self):
        garden = Garden()
        garden.gardenSize = 300

        return garden

    def getHeating(self):
        heating = Heating()
        heating.heatingType = "Samsung"
        heating.heatingPower = 3

        return heating

    def getGarage(self):
        garage = Garage()
        garage.numberOfCars = 50

        return garage

    def getSwimmingPool(self):
        swimmingPool = SwimmingPool()
        swimmingPool.swimmingPoolSize = 400
        
        return swimmingPool