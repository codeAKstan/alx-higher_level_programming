#!/usr/bin/python3
import hidden_4


def print_mod_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    for name in names:
        print(name)


if __name__ == "__main__":
    print_mod_names(hidden_4)
