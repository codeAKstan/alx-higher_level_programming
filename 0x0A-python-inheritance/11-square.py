#!/usr/bin/python3
""" task 10 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class square inheriting frm Rectangle"""

    def __init__(self, size):
        """ constructor """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
