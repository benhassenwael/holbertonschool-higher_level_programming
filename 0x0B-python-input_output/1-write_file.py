#!/usr/bin/python3
""" Module implementing a single function write_file """


def write_file(filename="", text=""):
    """ Writes a string to a text file and returns
        the number of characters written

    Args:
        filename: a string representing the file name
        text: the text to be written in the file

    Returns:
        the number of characters written
    """
    if filename:
        with open(filename, "w", encoding="utf8") as f:
            return f.write(text)

    return 0
