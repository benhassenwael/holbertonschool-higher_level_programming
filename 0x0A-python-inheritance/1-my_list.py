#!/usr/bin/python3
""" Module implementing a class that inherits from list """


class MyList(list):
    """ Class that extends list object with print_sorted method """
    def print_sorted(self):
        """ Print the list sorted (ascending) """
        print(sorted(self))
