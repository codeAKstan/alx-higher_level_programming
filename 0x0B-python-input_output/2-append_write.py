#!/usr/bin/python3
""" Append a file """


def append_write(filename="", text=""):
    """ a func that appends a string """

    with open(filename, 'a', encoding='utf-8') as f:
        append_content = f.write(text)
        return append_content
