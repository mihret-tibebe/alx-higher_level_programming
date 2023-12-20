#!/usr/bin/python3
"""Square with size

Practicing private attributes within a class and public method

"""


class Square:
    """Square with size attribute, throws exceptions if size is not valid
    and with a public method that returns the area
    """
    def __init__(self, size=0, position=(0, 0)):
        """ _size is initialized with size
        Args:
            size (int): size of the side of the square, should be greater
            than zero, ValueError is raised. If it's not an integer,
            a TypeError is raised.
            position (tuple):
        Attributes:
            size (int): the size of the square of this class set
            by the initializer.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position[0]) is not int or type(position[1]) is not int or \
                position[0] < 0 or position[1] < 0 or type(position) is not \
                tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates the area of this square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a visual representation of the square

        Print #'s according to the length of the side of the square,
        adds space on each line if position[1] is not greater than 0.
        self.__size

        """
        print() if self.size == 0 else None
        print('\n' * self.position[1], end="")
        for x in range(self.size):
            for y in range(self.position[0]):
                print(' ', end="")
            for y in range(self.size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Get private attribute size
        Returns:
            The attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets this.__size to value
        Args:
            value (int): the integer that will be set to size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get private attribute position
        Returns:
            The attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is not int or type(value[1]) is not \
                int or value[0] < 0 or value[1] < 0 or type(value) is not \
                tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
