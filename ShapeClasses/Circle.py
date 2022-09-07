from Shape import Shape
class Circle(Shape):
    """
    Circle Class: Yigveni
    """
    def __init__(self,base,pi):
        Shape.__init__(self,base)
        #self.base = base
        self.pi = 3.14

    def get_area(self):
        self.area = (self.pi * self.base ** 2)
        return f"The area is: {self.area}"

a = Circle(5,5)
print(a.get_area())
