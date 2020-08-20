class SubSystemA:
    def subOperation(self):
        print("This is the subOperation of the subSystemA.\n")

class SubSystemB:
    def subOperation(self):
        print("This is the subOperation of the subSystemB.\n")

class SubSystemC:
    def subOperation(self):
        print("This is the subOperation of the subSystemC.\n")

class Facade:
    def __init__(self):
        self._subA = SubSystemA()
        self._subB = SubSystemB()
        self._subC = SubSystemC()

    def operation1(self):
        self._subA.subOperation()
        self._subB.subOperation()

    def operation2(self):
        self._subC.subOperation()

    