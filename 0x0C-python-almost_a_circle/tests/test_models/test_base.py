#!/usr/bin/python3
""" Unit test for class Base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBase(unittest.TestCase):
    """Testing class Base functionality"""
    def test_id(self):
        """Test for id property"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

    def test_to_from_json_string(self):
        """Test for conversion of Base subclasses to json representation.
            Assumes that subclasses have implemented `to_dictionary()` method.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        json_dict = Base.to_json_string([r1_dict])
        self.assertEqual(r1_dict, {'x': 2,
                                   'width': 10,
                                   'id': 1,
                                   'height': 7,
                                   'y': 8})
        self.assertIs(type(r1_dict), dict)
        self.assertIs(type(json_dict), str)
        self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                           '"width": 10, '
                                                           '"id": 1, '
                                                           '"height": 7, '
                                                           '"y": 8}]'))
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIs(type(json_list_input), str)
        self.assertIs(type(list_output), list)
        self.assertEqual(list_output, list_input)
        self.assertEqual(json.loads(json_list_input),
                         json.loads('[{"height": 4, '
                                    '"width": 10, '
                                    '"id": 89}, '
                                    '{"height": 7, '
                                    '"width": 1, '
                                    '"id": 7}]'))
