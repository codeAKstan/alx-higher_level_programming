#!/usr/bin/python3
""" Write file """


def write_file(filename="", text=""):
    """ A func that writes a string to a text file """

    with open(filename, 'w', encoding='utf-8') as f:
        write_content = f.write(text)
        return write_content
