"""a python file for rectangle"""

from models.base import Base 

class Rectangle(Base):
    """
    a Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initilaize a new Rectangle
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))

        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        
    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

       
    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
    
    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")