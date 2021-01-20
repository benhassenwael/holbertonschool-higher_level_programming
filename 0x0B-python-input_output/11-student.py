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

    def to_json(self, attrs=None):
        """ Returning dictionary representation
            of instance attributes
        """
        if attrs and type(attrs) is list:
            dict_attr = {}
            for attr in self.__dict__:
                if attr in attrs:
                    dict_attr[attr] = self.__dict__[attr]
            return dict_attr

        return dict(self.__dict__)

    def reload_from_json(self, json):
        """ Replaces all attributes of the instance """
        self.__dict__.update(json)
