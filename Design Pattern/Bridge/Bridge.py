# This is the Bridge Design Pattern in Python

# The remote control class with some methods.
class RemoteControl:
    
    __device = None
    
    def __init__(self, device):
        self.__device = device
    
    def togglePower(self):
        print("Hit the toggle power")
        if self.__device.isEnabled():
            print("Disabling the device")
            self.__device.disable()
        else:
            print("Enabling the device")
            self.__device.enable()
        
    def volumeDown(self):
        self.__device.setVolume(self.__device.getVolume() - 10)

    def volumeUp(self):
        self.__device.setVolume(self.__device.getVolume + 10)

    def channelDown(self):
        self.__device.setChannel(self.__device.setChannel() - 1)

    def channelUp(self):
        self.__device.setChannel(self.__device.setChannel() + 1)

# Remote with some advanced features.
class AdvancedRemoteControl(RemoteControl):
    
    __device = None

    def soundMute(self):
        self.__device.setVolume(0)

# The Device interface.
class Device:
    def isEnabled(self): pass
    def enable(self): pass
    def disable(self): pass
    def getVolume(self): pass
    def setVolume(self, percent):pass
    def getChannel(self): pass
    def setChannel(self, channel): pass

class Tv(Device):
    def __init__(self):
        print("From the TV claas.")

class Radio(Device):
    def __init__(self):
        print("From the Radio class.")

def main():
    tv = Tv()
    remote = RemoteControl(tv)
    remote.togglePower()

if __name__ == "__main__":
    main()