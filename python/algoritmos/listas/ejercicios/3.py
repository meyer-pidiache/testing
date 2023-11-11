"""
Se tiene una lista simplemente ligada, con un dato numérico en cada nodo. Elabore un método que determine e imprima el promedio de datos de la lista.
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

    def print_average(self):
        node = self.head
        sum = 0
        count = 0
        while node:
            sum += node.data
            count += 1
            node = node.next
        print(f'El promedio de los datos de la lista es: {sum / count}')

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
linked_list.insert_at_end(1)

linked_list.print_list()
linked_list.print_average()

