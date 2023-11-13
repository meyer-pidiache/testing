"""
Elabore un método que intercambie los registros de una lista doblemente ligada así: el primero con el último, el segundo con el penúltimo, el tercero con el antepenúltimo, y así sucesivamente.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert_at_start(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print('None')

    # Es lo mismo que pide el enunciado, al intercambiar, la lista queda inversa
    def reverse_list(self):
        if self.head is None:
            return
        
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        self.head, self.tail = self.tail, self.head


linked_list = DoublyLinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_start(4)
linked_list.insert_at_start(5)
linked_list.insert_at_start(6)

linked_list.print_list()

linked_list.reverse_list()

linked_list.print_list()
