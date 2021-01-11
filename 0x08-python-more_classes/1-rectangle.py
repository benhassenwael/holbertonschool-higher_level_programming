#!/usr/bin/python3
""" This module contains a class rectangle
    for the purpose of practecing OOP """


class Rectangle:
    """ class Rectangle definition """
    def __init__(self, width=0, height=0):
        """ instance initilization

            Args:
                width: positive integer
                height: positive integer
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter of the private field width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter of the private field width

            Args:
                width: positive integer
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ Getter of the private field height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter of the private field height

            Args:
                height: positive integer
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
