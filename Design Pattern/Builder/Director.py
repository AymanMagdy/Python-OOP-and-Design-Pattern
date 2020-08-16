import json
from json import JSONEncoder

from Builder import Builder
from Apartment import Apartment
from Palace import Palace
from House import House

from PalaceBuilder import PalaceBuilder
from HouseBuilder import HouseBuilder
from ApartmentBuilder import ApartmentBuilder

# The builder Design Pattern

# Create House
# Create Palace
# Create Apartment

class Director:
    # Controls the construction process.
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPalace(self):
        palace = Palace()
        doors = self.__builder.getDoors()
        gardenSize = self.__builder.getGarden()
        heating = self.__builder.getHeating()
        heatingPower = heating.heatingPower
        heatingType = heating.heatingType
        swimmingPool = self.__builder.getSwimmingPool()

        # Build the palace
        palace.setDoors(doors)
        palace.setGarden(gardenSize)
        palace.setHeating(heatingType, heatingPower)
        palace.setSwimmingPool(swimmingPool)

        return palace

    def getHouse(self):
        house = House()
        doors = self.__builder.getDoors()
        gardenSize = self.__builder.getGarden()
        heating = self.__builder.getHeating()
        heatingPower = heating.heatingPower
        heatingType = heating.heatingType
        swimmingPool = self.__builder.getSwimmingPool()

        # Build the house
        house.setDoors(doors)
        house.setGarden(gardenSize)
        house.setHeating(heatingType, heatingPower)
        house.setSwimmingPool(swimmingPool)

        return house
    
    def getApartment(self):
        apartment = Apartment()
        doors = self.__builder.getDoors()
        heating = self.__builder.getHeating()
        heatingPower = heating.heatingPower
        heatingType = heating.heatingType

        # Build the palace
        apartment.setDoors(doors)
        apartment.setHeating(heatingType, heatingPower)

        return apartment

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__   


def main():
    palaceBuilder = PalaceBuilder()
    houseBuildr = HouseBuilder()
    apartmentBuilder = ApartmentBuilder()

    director = Director()

    director.setBuilder(apartmentBuilder)
    apartment = director.getApartment()

    print(MyEncoder().encode(apartment))

if __name__ == "__main__":
    main()