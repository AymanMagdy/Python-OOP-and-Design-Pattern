from Builder import Builder, Doors, Garage, Heating, SwimmingPool

class HouseBuilder(Builder):
    def getDoors(self):
        doors = Doors()
        doors.numberOfDoors = 5

        return doors

    def getGarden(self):
        garden = Garden()
        garden.gardenSize = 100

        return garden

    def getHeating(self):
        heating = Heating()
        heating.heatingType = "Union Air"
        heating.heatingPower = 3

        return heating

    def getGarage(self):
        garage = Garage()
        garage.numberOfCars = 3

        return garage

    def getSwimmingPool(self):
        swimmingPool = SwimmingPool()
        swimmingPool.swimmingPoolSize = 100
        
        return swimmingPool