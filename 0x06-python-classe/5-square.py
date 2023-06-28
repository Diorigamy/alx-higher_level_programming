#!/usr/bin/python3
""" defining a Square class """

class Square():
    """Square class"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
        size = self.size

    @property
     """property decorator"""
    def size(self):
        return self.__size

    @size.setter
    """setting property"""
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
          value =  self.__size
            
    def area(self):
        """calculating a squares area"""
        return self.__size ** 2

    def my_print(self):
        """print function"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
