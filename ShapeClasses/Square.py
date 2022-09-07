from Shape import Shape

class Rectangle(Shape):
    """
    Rectangle Class: Yishay
    """
    def __init__(self,base,area=0):
        Shape.__init__(self, base)
        self.area = area


    def getarea(self):
        self.area = (self.base*self.base)
        return self.area

a = Rectangle(5)
print(a)
print(a.get_area())