#!/usr/bin/python3
""" Module implementing the BaseGeometry class """


class BaseGeometry():
    """ Empty class """
    def area(self):
        """ Placeholder method for future implementation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate value

        Args:
            name: a string, name of the value
            value: what is valideted for being
                   apositive non zero integer

        Raises:
            TypeError: if value is not an int
            ValueError: if value is 0 or less
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
