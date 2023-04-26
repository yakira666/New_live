class StackObj:
    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if (isinstance(self.__next, StackObj)) or (self.__next is None):
            self.__next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        new_node = obj
        cur_data = self.top
        if cur_data is None:
            self.top = new_node
            return
        while cur_data.next is not None:
            cur_data = cur_data.next
        cur_data.next = new_node

    def pop(self):
        cur_data = self.top
        if cur_data is None:
            return cur_data
        elif cur_data.next is None:
            self.top = None
            return cur_data
        else:
            while cur_data.next.next is not None:
                cur_data = cur_data.next
            cur_data.next = None
            return cur_data

    def get_data(self):
        list_data = []
        cur_data = self.top
        if cur_data is None:
            return []
        while cur_data is not None:
            list_data.append(cur_data.data)
            cur_data = cur_data.next
        return list_data


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
st.pop()
st.pop()
res = st.get_data()  # ['obj1', 'obj2']
print(res)
