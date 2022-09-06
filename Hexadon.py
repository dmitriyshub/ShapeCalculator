from Shape import Shape
import math

class Hexadon(Shape):
    def __init__(self, args):
        super().__init__(args)

    def get_area(self, args):
        return ((3 * math.sqrt(3) * (args * args)) / 2)


c = Hexadon(5)
ans = c.get_area(5)
print(ans)





a = 1,2,3,4,5,6
b = Hexadon(a)
b.print_args(a)