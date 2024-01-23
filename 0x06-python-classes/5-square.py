#!/usr/bin/python3
"""Square module"""


class Square:
    """defining Square Class"""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            the size squared
        """
        return self.__size ** 2

    @property
    def size(self):
        """a getter to retrieve the size

        Returns: the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """a setter to change the size value
        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not int
            ValueError: if size is less than 0
        """
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Prints a square pattern of '#' characters based on the size."""

        if (self.__size == 0):
            print('')
        for i in range(self.__size):
            for i in range(self.__size):
                print('#', end="")
            print('')
