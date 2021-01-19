#!/usr/bin/python3
""" Module implementing the Square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Definition of class Square """
    def __init__(self, size):
        """ instance initilization

            Args:
                size: size of the square must be
                      positive non 0 integer
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculate and return the area of this square """
        return self.__size ** 2
