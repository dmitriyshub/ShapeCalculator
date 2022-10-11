from Hexadon import Hexadon
from Rectangle import Rectangle
from Circle import Circle
from Triangle import Triangle



def main():
    a = Hexadon(5)
    a.get_area()
    print(a.get_area())
    print(a)

    b = Triangle(10,10)
    print(b.get_area())
    print(b)


if __name__ == '__main__':
    main()