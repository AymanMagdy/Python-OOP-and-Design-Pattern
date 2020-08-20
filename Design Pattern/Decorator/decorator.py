class Component:
    def operation(self):
        pass

class ConcreteComponent:
    def __init__(self):
        Component.__init__(self)
    
    def operation(self):
        print("Concrete Component operation")

class Decorator(Component):
    def __init__(self, component):
        Component.__init__(self)
        self._component = component
    
    def operation(self):
        self._component.operation()

class ConcreteDecoratorA(Decorator):
  def __init__(self, component):
    super().__init__(component)
  
  def operation(self):
    super().operation()
    print("Decorator A")

class ConcreteDecoratorB(Decorator):
  def __init__(self, component):
    super().__init__(component)
  
  def operation(self):
    super().operation()
    print("Decorator B")