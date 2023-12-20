#!/usr/bin/python3
""" A class square based off 1-sqaure"""


class Square:
    """ A python class"""

    def __init__(self, size=0):
        """  constructor of class square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
