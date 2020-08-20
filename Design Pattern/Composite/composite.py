class Component():
    def __init__(self, *args, **kw):
        pass
    def component_function(self):
        pass

class Leaf(Component):
    def __init__(self, *args, **kw):
        super().__init__(self, *args, **kw)
    
    def component_function(self):
        print("Doing some function..")

class Composite(Component):
    def __init__(self, *args, **kw):
        Component.__init__(self, *args, **kw)
        self.children = []
    
    def append_child(self, child):
        self.children.append(child)
    
    def component_function(self):
        map(lambda x: x.component_function(), self.children)

c = Composite()
l = Leaf()
l_two = Leaf()
c.append_child(l)
c.append_child(l_two)
c.component_function()