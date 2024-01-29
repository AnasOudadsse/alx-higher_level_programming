#!/usr/bin/python3
""" square module """


class Rectangle:
    """
     This class defines a rectangle and provides methods to calculate its area and perimeter.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):

        """
        Initializes a new instance of the Rectangle class.

        Parameters:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """

        self._width = width
        self._height = height

    @property
    def width(self):

        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return self._width

    @width.setter
    def width(self, value):

        """
        Set the width of the rectangle.

        Parameters:
            value (int): The new width value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if (self._width < 0):
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):

        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self._height

    @height.setter
    def height(self, value):

        """
        Set the height of the rectangle.

        Parameters:
            value (int): The new height value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if (self._height < 0):
            raise ValueError('height must be >= 0')
        self._height = value
