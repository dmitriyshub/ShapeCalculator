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

  def get_area(self):

      area = (self.pi * self.radius ** 2)
      return f"The area is: {area}"

a= Circle(10)
print(a.get_area())