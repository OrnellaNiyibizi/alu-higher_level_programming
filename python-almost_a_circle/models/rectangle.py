#!/usr/bin/python3
"""Rectangle class inheriting"""


from models.base import Base


class Rectangle(Base):
    """"
        Class Rectangle inheriting Base
        Attr :
                id: number
                width: number
                height: number
                x: number
                y: number
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width has to be an integer")
        if value <= 0:
            raise ValueError("width has to be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height has to be an integer")
        if value <= 0:
            raise ValueError("height has to be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) != int:
            raise TypeError("x has to be an integer")
        if value < 0:
            raise ValueError("x has to be >= 0")
        self.__x = value

    @property
    def y(self):
        """get x"""
        return self.__y

    @y.setter
    def y(self, value):
        """set x"""
        if type(value) != int:
            raise TypeError("y has to be an integer")
        if value < 0:
            raise ValueError("y has to be >= 0")
        self.__y = value

    def area(self):
        """rectangle area"""
        return self.width * self.height

    def display(self):
        """the rectangle with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """ [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)
            
    def update(self, *args, **kwargs):
        """gives an argument"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            self.id = kwargs["id"] if "id" in kwargs else self.id
            self.width = kwargs["width"] if "width" in kwargs \
                else self.width
            self.height = kwargs["height"] if "height" in kwargs \
                else self.height
            self.x = kwargs["x"] if "x" in kwargs else self.x
            self.y = kwargs["y"] if "y" in kwargs else self.y

    def to_dictionary(self):
        """the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
