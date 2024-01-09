# #!/usr/bin/python3
# """rectangle class
# """


# class Rectangle():
#     """rectangle class
#     """
#     def __init__(self, width=0, height=0):
#         if type(width) is not int:
#             raise TypeError("height must be an integer")
#         if width < 0:
#             raise ValueError("height must be >= 0")
#         self.__width = width

#         if type(height) is not int:
#             raise TypeError("height must be an integer")
#         if height < 0:
#             raise ValueError("height must be >= 0")
#         self.__height = height

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, value):
#         if type(value) is not int:
#             raise TypeError("width must be an integer")
#         if value < 0:
#             raise ValueError("width must be >= 0")
#         self.__width = value

#     @property
#     def height(self):
#         return self.__height

#     @height.setter
#     def height(self, value):
#         if type(value) is not int:
#             raise TypeError("height must be an integer")
#         if value < 0:
#             raise ValueError("height must be >= 0")
#         self.__height = value



#!/usr/bin/python3

"""
Module containing class Rectangle
"""


class Rectangle:
    """
    A rectangle that has a width and height. Both are 0 by default.
    """

    def __init__(self, width=0, height=0):
        """
        width and height are initialized here. Appropriate error is printed if
        passed vars are incorrect

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Attributes:
            width (int): width of rectangle, initialized by constructor
            height (int): height of rectangle, initialized by constructor
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Get private attribute width
        Returns:
            The attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private attribute width to value, or raises an exception
        if value doesn't meet the requirements
        Args:
            value (int): the new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get private attribute height
        Returns:
            The attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the private attribute height to value, or raises an exception
        if value doesn't meet the requirements
        Args:
            value (int): the new value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
