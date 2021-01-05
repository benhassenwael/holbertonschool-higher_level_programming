#!/usr/bin/python3
""" This module is used as intro to classes """


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
