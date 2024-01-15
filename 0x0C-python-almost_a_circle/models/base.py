#!/usr/bin/python3
""" Base class """


class Base:
    """ this class will be the base of all classes of this project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ a constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
