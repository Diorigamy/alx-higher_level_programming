#!/usr/bin/python3
""" defining a Square class """

class Square():
    """Square class"""

    def __init__(self,size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
        size = self.size
