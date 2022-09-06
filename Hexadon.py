from Shape import Shape
import math

class Hexadon(Shape):
    """
    Hexadon class: Dima
    """
    def __init__(self, args):
        super().__init__(args)

    def get_area(self):
        area = ((3 * math.sqrt(3) * (self.args * self.args)) / 2)
        return area


c = Hexadon(10)
print(c)
ans = c.get_area()
print(ans)





# a = 1,2,3,4,5,6
# b = Hexadon(a)
# b.print_args(a)