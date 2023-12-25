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

       
    