import random
class Circle:
  """
  Create a Circle class.
- A Circle class gets a radius.
- Set a constructor, get and set functions of that radius.
- Write a function that calculates it area.
- Write a function that calculates it perimeter
  """
  def __init__(self,radius):
      self.radius = radius
      self.pi = 3.14

  def __str__(self):
      return f'The area of this {self.__class__.__name__} is {self.get_area()}\n' \
             f'The radius of this {self.__class__.__name__} is {self.get_perimiter()}'

  def get_area(self):
      self.area = (self.pi * self.radius ** 2)
      return self.area

  def get_perimiter(self):
      self.perimiter = 2 * self.pi*self.radius
      return self.perimiter

a= Circle(10)
print(a)
print(a.get_area())
print(a.get_perimiter())

class Square:
    """
  Create a Square class.
- A Square class gets the length of a side.
- Set a constructor, get and set functions of that side.
- Write a function that calculates it area.
- Write a function that calculates it perimeter.
    """
    def __init__(self,length):
        self.length=length

    def __str__(self):
        return f'The area of this {self.__class__.__name__} is {self.get_area()}\n' \
               f'The perimiter of this {self.__class__.__name__} is {self.get_perimiter()}'

    def get_area(self):
        self.area = self.length * self.length
        return self.area

    def get_perimiter(self):
        self.perimiter = 4 * self.area
        return self.perimiter

b= Square(10)
print(b)
print(b.get_area())
print(b.get_perimiter())

