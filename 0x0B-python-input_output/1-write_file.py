#!/usr/bin/python3
"""defines a text file writing function"""


def write_file(filename="", text=""):
    """writes a string to a text file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written
    """

    with open(filename, mode='w', encoding="utf-8") as fl:
        return fl.write(text)
