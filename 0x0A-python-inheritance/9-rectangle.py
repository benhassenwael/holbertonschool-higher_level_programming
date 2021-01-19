#!/usr/bin/python3
""" Module implementing the Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Definition of class Rectangle """
    def __init__(self, width, height):
        """ instance initilization
            Args:
                width: positive integer
                height: positive integer
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate and return the area of this rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string for printing the Rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
