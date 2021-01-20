#!/usr/bin/python3
""" Module implementing class Student """


class Student():
    """ Rpresenting a student with:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """ Initializing new instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returning dictionary representation
            of instance attributes
        """
        return dict(self.__dict__)
