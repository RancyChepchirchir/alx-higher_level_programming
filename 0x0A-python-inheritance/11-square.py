#!/usr/bin/python3
"""Module: 11-square
This is a class Square that inherits from Rectangle class as the base class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a format string of the attribute size"""

        return("[Square] {}/{}".format(self.__size, self.__size))
    
    def area(self):
        """Returns the area of the Square instance"""

        return self.__size **2