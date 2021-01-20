#!/usr/bin/python3
""" Module implementing a single function append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file,
        after each line containing a specific string

    Args:
        filename: a string representing the file name
        search_string: string to insert in the line after
        new_string: the text to be written in the file
    """
    if filename:
        with open(filename, "r", encoding="utf8") as f:
            text = [line for line in f]

        with open(filename, "w", encoding="utf8") as f:
            for line in text:
                if line.find(search_string) >= 0:
                    line = line + new_string
                f.write(line)
