"""
Elabore un método que intercambie los registros de una lista doblemente ligada así: el primero con el tercero, el segundo con el cuarto, el quinto con el séptimo, el sexto con el octavo, y así sucesivamente.
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

    def swap_list(self):
        current = self.head

        while current.next.next is not None:
            data_bak = current.data
            current.data = current.next.next.data
            current.next.next.data = data_bak
            # Intercambiar nodos
            current = current.next

# Crear una lista doblemente ligada
linked_list = DoublyLinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_start(4)
linked_list.insert_at_start(5)
linked_list.insert_at_start(6)

print("Lista original:")
linked_list.print_list()

linked_list.swap_list()

print("\nLista después de intercambiar elementos:")
linked_list.print_list()

