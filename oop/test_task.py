class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


s = Node(1)
q = s
for i in range(3, 10):
    o = Node(i)
    q.next = o
    q = o



