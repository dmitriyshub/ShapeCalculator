from Shape import Shape

class Rectangle(Shape):
    """
    Rectangle Class: Yishay
    """
    def __init__(self,base):
        Shape.__init__(self, base)
        self.area = 0


    def get_area(self):
        self.area = (self.base*self.base)
        return self.area

a = Rectangle(5)
print(a)
print(a.get_area())