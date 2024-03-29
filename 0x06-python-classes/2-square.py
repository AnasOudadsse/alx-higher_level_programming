#!/usr/bin/python3
"""Square module"""


class Square:
    """defining Square Class"""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
