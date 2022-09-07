from Shape import Shape

class Rectangle(Shape):
    """
    Rectangle Class: Yishay
    """
    def __init__(self,base):
        Shape.__init__(self, base)


    def getarea(self):
        self.area = self.base*self.base
        return self.area

a = Rectangle(5)
print(a.get_area())
