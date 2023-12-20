#!/usr/bin/python3
""" A class based off 2-sqaure"""


class Square:
    """A python class"""

    def __init__(self, size=0):
        """A constructor"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """A public instance method"""

            return (self.__size * self.__size)
