#!/usr/bin/env python3
def no_c(my_string):
    remove_c = ""
    if my_string:
        for c in my_string:
            if c.lower() != 'c':
                remove_c += c
        return remove_c
