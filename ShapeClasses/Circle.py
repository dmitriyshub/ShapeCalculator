from Shape import Shape
class Circle(Shape):
    def __init__(self,radius):
        Shape.__init__(self)
        self.radius = radius
        self.pi = 3.14
    def get_area(self):
        self.area = (self.pi * self.radius ** 2)
        return print(f"The area is: {self.area}")