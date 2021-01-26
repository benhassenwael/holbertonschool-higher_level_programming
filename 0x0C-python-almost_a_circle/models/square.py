#!/usr/bin/python3
""" Module implementing Rectangle class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class representing a square with
        size, and spatial position x, y
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Instance initialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter of the private field size """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter of the private field size
            Args:
                size: positive integer
        """
        self.width = size
        self.height = size

    def __str__(self):
        """ Return string representation of
            the rectangle
        """
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(
                           self.id,
                           self.x,
                           self.y,
                           self.height
                       )

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if len(args):
            atts = ["id", "size", "x", "y"]
            for k, v in zip(atts, args):
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Returning dictionary representation
            of instance attributes
        """
        atts = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in atts}
