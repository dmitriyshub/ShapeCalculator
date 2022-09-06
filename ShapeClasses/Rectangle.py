from Shape import Shape

class Rectangle(Shape):
    """
    Rectangle Class: Yishay
    """
    def __init__(self, *args):
        Shape.__init__(self, args)
        self.args = args

    def getarea(self):
        return self.args[0]*self.args[1]

a = Rectangle
