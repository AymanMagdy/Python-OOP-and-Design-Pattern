from Builder import Builder, Doors, Garage, Heating

class ApartmentBuilder(Builder):
    def getDoors(self):
        doors = Doors()
        doors.numberOfDoors = 3

        return doors

    def getHeating(self):
        heating = Heating()
        heating.heatingType = "Hyper"
        heating.heatingPower = 3

        return heating

    def getGarage(self):
        garage = Garage()
        garage.numberOfCars = 2

        return garage

