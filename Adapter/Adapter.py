# This is a simple example of the Adapter Design Pattern

# The EU class iterface.
class EUSocketInterface:
    def voltage(self): pass

    def live(self): pass
    def netural(self): pass
    def earth(self): pass

# The socket that inhirets from the EU interface.
class Socket(EUSocketInterface):
    def voltage(self):
        return 230
    
    def live(self):
        return 1

    def netural(self):
        return -1
    
    def earth(self):
        return 0

# The US socket interface.
class USASocketInterface:
    def voltage(self): pass

    def live(self): pass
    def netural(self): pass

# The adapter that inherits from the US interface.
class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket
    
    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def netural(self):
        return self.__socket.netural()

# The kettle checker
class ElectricKettle:
    __power = None
    
    def __init__(self, power):
        self.__power = power
    
    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle is on fire..")
        else:
            if self.__power.live() == 1 and self.__power.netural() == -1:
                print("Coffee time..")
            else:
                print("No power.")

def main():
    # Plug in
    socket  = Socket()
    adapter = Adapter(socket)
    kettle  = ElectricKettle(adapter)

    # Make coffee
    kettle.boil()

    return 0

if __name__ == "__main__":
    main()