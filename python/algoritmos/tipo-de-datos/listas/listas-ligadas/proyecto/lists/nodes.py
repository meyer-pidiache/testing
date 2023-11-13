# Clases de nodos
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class DoubleNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None

