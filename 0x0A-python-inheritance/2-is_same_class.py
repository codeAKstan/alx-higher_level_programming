#!/usr/bin/python3
""" task 2, exacr same object """


def is_same_class(obj, a_class):
    """ checking if object is exactly an instance of the specified class
    """
    return type(obj) is a_class
