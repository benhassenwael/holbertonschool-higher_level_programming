#!/usr/bin/python3
""" This module contains a single function
    for the purpose of practecing doctests """


def text_indentation(text):
    """ Print a given text with 2 new lines
        after each of these characters: ., ? and :

    Args:
        text: a text to print

    Raises:
        TypeError: if 'text" is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    indent = ['.', '?', ':']
    for i in range(len(text)):
        if not (text[i] == ' ' and text[i - 1] in indent):
            print(text[i], end='')
        if text[i] in indent:
            print('\n')
