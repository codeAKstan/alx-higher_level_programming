#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ A func that reads a text file """

    with open(filename, encoding='utf-8') as f:
        read_content = f.read()
        print(read_content, end="")
