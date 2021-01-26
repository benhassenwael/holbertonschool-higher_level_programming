#!/usr/bin/python3
""" Module Implementing Base class """
import json
import csv


class Base:
    """ This class will be the “base” of all other
        classes in this project. The goal of it is
        to manage id attribute in all future classes
        and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instance initilization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """ Creates and returns an instance with all
            attributes already set

        Args:
            dictionary: instance attributes and values to be set
        """
        if cls.__name__ == "Square":
            new_inst = cls(1)
        else:
            new_inst = cls(1, 1)
        new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a list of Objects to a text
            file using JSON representation
        Args:
            list_objs: Objects list to wirite as a JSON in a file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf8") as f:
            if not list_objs:
                list_objs = []
            list_dict = [o.to_dictionary() for o in list_objs]
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file(cls):
        """ Creates a list of instances from a JSON file """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf8") as f:
                dict_list = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**o) for o in dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Writes a list of Objects to a text
            file using CSV representation
        Args:
            list_objs: Objects list to wirite as a CSV in a file
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", encoding="utf8") as f:
            if not list_objs:
                list_objs = []
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for o in list_objs:
                writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Creates a list of instances from a JSON file """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", encoding="utf8") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=fieldnames)
                list_objs = []
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    list_objs.append(cls.create(**row))
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON representation of
            dictionaries list

        Args:
            list_dictionaries: a list of dictionaries
        """
        if len(list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """ Return an object represented by a JSON string
        Args:
            json_string: JSON string to decode into an object
        Returns:
            Object
        """
        if not json_string:
            return []
        return json.loads(json_string)
