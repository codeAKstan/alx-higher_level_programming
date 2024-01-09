#!/usr/bin/python3
""" create object from json file """
import json


def load_from_json_file(filename):
    """ a function that creates an object from json file """

    with open(filename) as f:
        ret = json.load(f)
        return ret
