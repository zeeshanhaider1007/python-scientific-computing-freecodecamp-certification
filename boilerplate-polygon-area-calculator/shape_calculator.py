class Rectangle:
  def __init__(self, width=None, height=None):
    self.width = width
    self.height = height
  def set_width(self,width):
    self.width = width
  def set_height(self,height):
    self.height = height
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * (self.width + self.height)
  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture = picture + "*" * self.width  + "\n"
      return picture
  def get_amount_inside(self,shape):
    width_fit = self.width // shape.width
    height_fit = self.height // shape.height
    if width_fit == 0 or height_fit == 0:
      return 0
    return width_fit * height_fit
  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side=None):
    super().__init__(side,side)
    self.side = side
  def set_side(self,side):
    self.side = side
    self.set_width(side)
    self.set_height(side)
  def __str__ (self):
    return f"Square(side={self.side})"
  def set_width(self,width):
    self.width = width
    self.height = width
    self.side = width
  def set_height(self,height):
    self.width = height
    self.height = height
    self.side = height
    
    