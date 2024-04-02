#!/usr/bin/python3
"""
a script taht takes a url aend a request to the url
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
