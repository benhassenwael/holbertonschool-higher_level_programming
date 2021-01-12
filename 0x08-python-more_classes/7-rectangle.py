#!/usr/bin/python3
""" This module contains a class rectangle
    for the purpose of practecing OOP """


class Rectangle:
    """ class Rectangle definition """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ instance initilization

            Args:
                width: positive integer
                height: positive integer
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Calculate and return the rectangle's area """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculate and return the rectange's perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ Print Rectangle using the print_symbol character """
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for i in range(self.__height):
            s += str(self.print_symbol) * self.__width
            if i < (self.__height - 1):
                s += "\n"
        return s

    def __repr__(self):
        """ String representation of the object """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Clean up function invoked on instance deletion """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
