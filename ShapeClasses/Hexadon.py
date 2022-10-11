from Shape import Shape, math

class Hexadon(Shape):
    """
    Hexadon class: Dima
    """
    def __init__(self):
        super().__init__()

    def get_area(self,base):
        self.base = base
        self.area = 0

        self.area = ((3 * math.sqrt(3) * (self.base * self.base)) / 2)
        return self.area


c = Hexadon()
print(c)
ans = c.get_area(5555)
print(ans)





# a = 1,2,3,4,5,6
# b = Hexadon(a)
# b.print_args(a)