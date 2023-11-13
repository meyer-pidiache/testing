# Listas ligadas

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def delete(self, data):
        node = self.head
        if node and node.data == data:
            self.head = node.next
            return
        while node:
            if node.next and node.next.data == data:
                node.next = node.next.next
                return
            node = node.next

        print('Dato no encontrado')

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def sort_list(self):
        node = self.head
        while node:
            temp = node.next
            while temp:
                if node.data > temp.data:
                    node.data, temp.data = temp.data, node.data
                temp = temp.next
            node = node.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print('None')

# Creando una lista
linkedList = LinkedList()

# Insertando elementos
linkedList.insert_at_start(5)
linkedList.insert_at_start(1)
linkedList.insert_at_end(2)
linkedList.insert_at_end(3)
linkedList.insert_at_end(4)

print('Lista incial: ', end='')
linkedList.print_list()

# Eliminando elementos
linkedList.delete(1)

print('Lista actualizada: ', end='')
linkedList.print_list()

# Buscando elementos
print('Buscando el número 2: ', end='')
if linkedList.search(2):
    print('Dato encontrado')
else:
    print('Dato no encontrado')

# Ordenando la lista
linkedList.sort_list()

print('Lista ordenada: ', end='')
linkedList.print_list()

