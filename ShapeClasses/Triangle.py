from Shape import Shape
class Triangle(Shape):
    """
    Triangle Class : Omri
    """
    def __init__(self, base, height):
        Shape.__init__(self, base)
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2

    def __str__(self):
        return (f'the height of the triangle is {self.height} '
                f'\nthe base of the triangle is {self.base}'
                f'\nthe area of the triangle is {self.get_area()}')

b = Triangle(5,5)
print(b.get_area())