#!/usr/bin/python3
""" class rectangle """


class Rectangle:
    """ rectanle class """
    def __init__(self, width=0, height=0):
        """  constructor """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getting width """
        return self.__width

    @property
    def height(self):
        """ getting height """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
