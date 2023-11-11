"""
Elabore un método que borre de una lista simplemente ligada un dato dado todas las veces que lo encuentre.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def delete_all_coincidences(self, data):
        node = self.head
        if node and node.data == data:
            self.head = node.next
        while node:
            if node.next and node.next.data == data:
                node.next = node.next.next
            node = node.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print('None')

linked_list = LinkedList()
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(2)

linked_list.print_list()

linked_list.delete_all_coincidences(2)

linked_list.print_list()

