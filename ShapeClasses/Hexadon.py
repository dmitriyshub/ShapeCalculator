from Shape import Shape
import math

class Hexadon(Shape):
    """
    Hexadon class: Dima
    """
    def __init__(self, base):
        Shape.__init__(self,base)
        self.args=base

    def get_area(self):
        self.area = ((3 * math.sqrt(3) * (self.base * self.base)) / 2)
        return self.base


# c = Hexadon(10)
# print(c)
# ans = c.get_area()
# print(ans)





# a = 1,2,3,4,5,6
# b = Hexadon(a)
# b.print_args(a)