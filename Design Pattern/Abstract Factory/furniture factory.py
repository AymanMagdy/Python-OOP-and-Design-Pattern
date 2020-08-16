# Create Chair
# Create CoffeeTable
# Create Sofa

class Furniture():
    __productType = ""
    __productName = ""

    def __init__(self, productType, productName):
        self.__productType = productType
        self.__productName = productName

    def getProductType(self):
        return self.__productType
    
    def getProductName(self):
        return self.__productName

class ModernChair(Furniture):
    __productType = "Modern Chair"
    __productName = "Chair MMM"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)

class GetVictorianChair(Furniture):
    __productType = "Victorian Chair"
    __productName = "Chair VVV"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)

class ModernCoffeeTable(Furniture):
    __productType = "Modern Coffee Table"
    __productName = "Coffee Table MMM"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)

class VictorianCoffeeTable(Furniture):
    __productType = "Victorian Coffee Table"
    __productName = "Coffee Table MMM"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)

class VictorianChair(Furniture):
    __productType = "Victorian Coffee Table"
    __productName = "Coffee Table VVV"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)

class ModernSofa(Furniture):
    __productType = "Modern Sofa"
    __productName = "Sofa MMM"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)

class VictorianSofa(Furniture):
    __productType = "Victorian Sofa"
    __productName = "Sofa VVV"

    def __init__(self):
        super().__init__(self.__productType, self.__productName)


# Abstarct Factory
class FurnitureFactory:
    def getModernChair(self): pass
    def getModernCoffeeTable(self): pass
    def getModernSofa(self): pass

    def getVictorianChair(self): pass
    def getVictorianCoffeeTable(self): pass
    def getVictorianSofa(self): pass

class GetModernFurnitureFactory(FurnitureFactory):
    def getModernChair(self):
        return ModernChair()
    
    def getModernCoffeeTable(self):
        return ModernCoffeeTable()
    
    def getModernSofa(self):
        return ModernSofa()

class GetVictorianFurnitureFactory(FurnitureFactory):
    def getVictorianChair(self):
        return GetVictorianChair()
    
    def getVictorianSofa(self):
        return VictorianSofa()

    def getVictorianCoffeeTable(self):
        return VictorianCoffeeTable()

if __name__ == "__main__":
    productType = "modern"

    if productType == "victorian":
        chairFactory = GetVictorianFurnitureFactory()
    else:
        chairFactory = GetModernFurnitureFactory()

    # Build the chair
    chairFactoryObject = chairFactory.getModernSofa()

    print("Chair name: ", chairFactoryObject.getProductName())
    print("Chair type: ", chairFactoryObject.getProductType())
    