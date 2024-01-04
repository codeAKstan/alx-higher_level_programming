#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ public instance method area """
        return self.width * self.height

    def perimeter(self):
        """ return the perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ representation using # """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += "#" * self.width + '\n'
        return rect_str[:-1]

    def __repr__(self):
        """ string representation """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ deleting """
        print("Bye rectangle...")
