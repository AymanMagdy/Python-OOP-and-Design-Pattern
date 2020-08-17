import json
from DeliveryTypes import Palne, Ship, Truck

class Mail:

    delivelryType = ""

    def deliver(self, delivelryType, fromPlace, toPlace):
        self.delivelryType = delivelryType
        if (self.delivelryType == "Truck"):
            return Truck(fromPlace, toPlace)
        elif (self.delivelryType == "Plane"):
            return Palne(fromPlace, toPlace)
        elif (self.delivelryType == "Ship"):
            return Ship(fromPlace, toPlace)
        else:
            return None

    def getObj(self):
        pass


