#!/usr/bin/python3
""" Module implementing a single function append_write """


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file and returns
        the number of characters added

    Args:
        filename: a string representing the file name
        text: the text to be written in the file

    Returns:
        the number of characters written
    """
    if filename:
        with open(filename, "a", encoding="utf8") as f:
            return f.write(text)

    return 0
