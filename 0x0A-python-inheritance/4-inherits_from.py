#!/usr/bin/python3
""" task 4 """


def inherits_from(obj, a_class):
    """ returns true if the object is an instance of a class inherited
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
