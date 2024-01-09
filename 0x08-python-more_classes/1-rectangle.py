#!/usr/bin/python3
"""rectangle class
"""


class Rectangle():
    """rectangle class
    """
    def __init__(self, width = 0):
        self.__width = width

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
