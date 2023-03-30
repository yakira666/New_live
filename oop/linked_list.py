from node_for_linked import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return
        while cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node is not None:
            output += "[" + str(cur_node.get_data()) + "]" + "->"
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def push_front(self, data):
        cur_node = self.head
        if cur_node is not None:
            new_node = Node(data)
            new_node.set_next(cur_node)
            self.head = new_node

    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def remove_front(self):
        self.head = self.head.get_next()

    def value_at(self, index):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        return IndexError

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.push_front(data)
                return
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        else:
            raise IndexError

    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                cur_node.set_next(cur_node.get_next().get_next())
                return
            count += 1
            cur_node = cur_node.get_next()
        else:
            raise IndexError

    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node is not None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(4)
    my_list.append(8)
    my_list.append(16)
    my_list.show()
    my_list.length()
    my_list.push_front(255)
    my_list.show()
    my_list.remove_back()
    my_list.show()
    my_list.remove_front()
    my_list.insert(2, 9)
    my_list.show()
    my_list.remove(3)
    my_list.show()
    my_list.reverse()
    my_list.show()
