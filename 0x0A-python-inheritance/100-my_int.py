#!/usr/bin/python3
""" Module implementing the MyInt class """


class MyInt(int):
    """ A rebel class that inverts == and != operators """
    def __eq__(self, obj):
        """ Definition of == operator """
        return self.numerator != obj.numerator

    def __ne__(self, obj):
        """ Definition of != operator """
        return self.numerator == obj.numerator
