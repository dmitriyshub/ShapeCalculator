class Shape:
    """
    Main Shape Class
    """
    def __init__(self,  base):
        self.base = base
        #self.pi = pi


    def __str__(self):
        return f'The area of this {self.__class__.__name__} is {self.get_area()}'

    def get_area(self):
        pass




