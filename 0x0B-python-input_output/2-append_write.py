#!/usr/bin/python3
"""define a append to a file function"""


def append_write(filename="", text=""):
    """appends to the end of a file

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, mode='a', encoding='utf-8') as fl:
        return fl.write(text)
