"""
Elabore un método que lea un entero n y que construya una lista simplemente ligada, de a digito por nodo.
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
        
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print('None')


integer = int(input("Ingresa un número entero: "))

linked_list = LinkedList()

for i in str(integer):
    linked_list.insert_at_end(int(i))

linked_list.print_list()

