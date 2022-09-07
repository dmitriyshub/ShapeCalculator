from Shape import Shape

class Rectangle(Shape):

    def __init__(self, base, length):
        Shape.__init__(self, base)
        self.length = length

    def get_area(self):
        self.area = float(self.base) * float(self.length)
        return self.area

    def __str__(self):
        return (f"\n{__class__.__name__} length is: {self.length}\n\
        {__class__.__name__} breadth is: {self.base}\n\t\t\
        {__class__.__name__} area is: {self.area}")


a = Rectangle(5,10)

print(a.get_area())
