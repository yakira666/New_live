class ObjList:
    def __init__(self, data, next=None):
        self.__prev = None
        self.__data = data
        self.__next = next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_prev(self, prev):
        self.__prev = prev

    def set_data(self, data):
        self.__data = data

    def set_next(self, next):
        self.__next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """Добавление элементов в конец списка"""
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if self.head is None:
            self.head = obj

    def remove_obj(self):
        """Удаление последнего элемента"""
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        """Показ всех элементов"""
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s