#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    # constructor for the Rectangle class
    def __init__(self, width, height, x=0, y=0, id=None):
        # call the constructor of the Base class with the id argument
        super().__init__(id)
        # assign the width, height, x, and y arguments to their respective attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # getter and setter for the width attribute
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # getter and setter for the height attribute
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # getter and setter for the x attribute
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # getter and setter for the y attribute
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
