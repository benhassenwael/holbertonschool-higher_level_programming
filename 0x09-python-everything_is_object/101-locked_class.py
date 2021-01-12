#!/usr/bin/python3
""" Module implementing LockedClass class """


class LockedClass:
    """LockedClass demonstrates the use of the __slots__ attribute

    Attributes:
        __slots__: List of strings which may serve as valid attribute
            identifiers as in `self.__dict__`.
    """
    __slots__ = ['first_name']
