#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError()
    except TypeError as err:
        raise err

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")