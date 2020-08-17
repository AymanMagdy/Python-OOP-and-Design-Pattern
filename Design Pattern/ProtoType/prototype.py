import copy

class Prototype:
    
    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type
    
    def getValue(self):
        return self._value

class ObjectFactory:

    __type1Value1 = None
    __type1Value2 = None
    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def intialize():

        ObjectFactory.__type1Value1 = Type1(11)
        ObjectFactory.__type1Value2 = Type1(12)
        ObjectFactory.__type2Value1 = Type2(21)
        ObjectFactory.__type2Value2 = Type2(22)

    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()

class Type1(Prototype):

    def __init__(self, number):
        self._type = "Type1"
        self._value = number
    
    def clone(self):
        return copy.copy(self)

class Type2(Prototype):

    _type = ""
    _value = ""

    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy.copy(self)

def main():
    ObjectFactory.intialize()
    instance = ObjectFactory.getType1Value1()

    print("Type: ", instance.getType())
    print("Value: ", instance.getValue())    

if __name__ == "__main__":
    main()