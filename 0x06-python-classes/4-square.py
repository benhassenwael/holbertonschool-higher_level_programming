#!/usr/bin/python3
class Square:
    """ square class with size(>=0 integer) attribute """
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")


    @property
    def size(self):
        """ size attibute getter """
        return self.__size


    @size.setter
    def size(self, value):
        """ size attribute setter """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")


    def area(self):
        """ calculate and return the area of the square """
        return self.__size ** 2
