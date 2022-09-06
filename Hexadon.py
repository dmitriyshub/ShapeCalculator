from Shape import Shape
import math

class Hexadon(Shape):
    def __init__(self, args):
        super().__init__(args)

    def get_area(self):
        return ((3 * math.sqrt(3) * (self.args * self.args)) / 2)

a = 5
c = Hexadon(a)

ans = c.get_area()
print(ans)





# a = 1,2,3,4,5,6
# b = Hexadon(a)
# b.print_args(a)