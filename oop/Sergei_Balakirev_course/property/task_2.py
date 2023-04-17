class WindowDlg:
    def __init__(self, title, width, height):
        self.__title: str = title
        self.__width: int = width
        self.__height: int = height

    def show(self):
        print(f"{self.__title}:{self.__width},{self.__height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if 0 <= width <= 10000:
            if self.__width is None:
                self.__width = width
                return
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if 0 <= height <= 10000:
            if self.__height is None:
                self.__height = height
                return
            self.__height = height
            self.show()
