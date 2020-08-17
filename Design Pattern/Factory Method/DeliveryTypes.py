import json
from Mail import Mail

class Palne(Mail):
    
    fromCountry = ""
    toCountry = ""
    planJsn = ""

    def __init__(self, fromCountry, toCountry):
        self.fromCountry = fromCountry
        self.toCountry = toCountry

        planJsn = {
            "Delivery Type": "Plane",
            "From": self.fromCountry,
            "To": self.toCountry
        }

        self.planJsn = planJsn

    def getObj(self):
        return json.dumps(self.planJsn)

class Truck(Mail):

    fromCity = ""
    toCity = ""
    truckJsn = ""

    def __init__(self, fromCity, toCity):
        self.fromCity = fromCity
        self.toCity = toCity

        truckJsn = {
            "Delivery Type": "Truck",
            "From": self.fromCity,
            "To": self.toCity
        }

        self.truckJsn = truckJsn
    
    def getObj(self):
        return json.dumps(self.truckJsn)

class Ship(Mail):

    fromPort = ""
    toPort = ""
    shipJsn = ""

    def __init__(self, fromPort, toPort):
        self.fromPort = fromPort
        self.toPort = toPort

        shipJsn = {
            "Delivery Type": "Ship",
            "From": self.fromPort,
            "To": self.toPort
        }

        self.shipJsn = shipJsn

    def getObj(self):
        return json.dumps(self.shipJsn)