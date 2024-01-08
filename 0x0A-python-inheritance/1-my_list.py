#!/usr/bin/python3
""" 1-mylist task 1 """


class MyList(list):
    """ A class that inherits from list """
    def __init__(self):
        """ constructor """
        super().__init__()

    def print_sorted(self):
        """ prints list in ascending sort """
        print(sorted(self))
