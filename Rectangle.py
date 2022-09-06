from Shape import Shape

class Rectangle(Shape):
    def __init__(self, args):
        super().__init__(args)

    def get_area(self, args):
        pass

a = 1,2,3,4,5,6
b = Rectangle(a)
b.print_args(a)