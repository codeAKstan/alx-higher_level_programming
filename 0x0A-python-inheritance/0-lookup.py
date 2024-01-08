#!/usr/bin/python3
""" 0-lookup, task 1 """


def lookup(obj):
    """ A function that returns the
    lisr of available attributes and methods of an object
    """
    return [attr for attr in dir(obj)
            if not callable(getattr(obj, attr)) or attr.startswith("__")]
