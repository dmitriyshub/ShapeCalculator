class Shape:
    def __init__(self, args):
        self.args = args

    def print_args(self,args):
        print(f'{args}')

    def get_area(self):
        pass












class Rectangle(Shape):
    def __init__(self, args):
        super().__init__(args)

    def get_area(self, args):
        pass


