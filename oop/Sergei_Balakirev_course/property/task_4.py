class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0.0, y=0.0):
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check(y):
            self.__y = y

    @classmethod
    def __check(cls, g):
        return ((type(g) is int) or (type(g) is float)) and (cls.MIN_COORD <= g <= cls.MAX_COORD)

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)
