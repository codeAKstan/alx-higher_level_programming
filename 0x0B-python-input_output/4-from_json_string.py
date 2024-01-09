#!/usr/bin/python3
""" From json string to object """
import json


def from_json_string(my_str):
    """ A func that returns an object """

    e = json.loads(my_str)
    return e
