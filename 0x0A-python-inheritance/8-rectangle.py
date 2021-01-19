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
