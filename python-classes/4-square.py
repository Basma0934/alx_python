"""Define a class Square."""

class Square():
    """write a class that defines a square by private instance attribute: size."""

    def __init__(self, size=0):
    
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
    
    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def my_print(self):
        """Print in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        