from lists.nodes import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.size += 1

    def dequeue(self):
        if self.first is None:
            print("La cola está vacía")
        else:
            removed_node = self.first
            self.first = self.first.next
            self.size -= 1
            print(f"Valor desencolado: {removed_node.value}")

    def get_first(self):
        if self.first == None:
            print("La cola está vacía")
        else:
            print(f"Primero en la cola: {self.first.value}")

    def is_empty(self):
        if self.first == None:
            print("La cola está vacía")
        else:
            print("La cola no está vacía")

    def get_size(self):
        print(f"Tamaño de la cola: {self.size}")

    def menu(self):
        option = 0
        while option != 6:
            print("""
            COLA

            Seleccione una opción:
                1) Encolar
                2) Desencolar
                3) Mostrar primero en la cola
                4) ¿Está vacía?
                5) Mostrar tamaño
                6) Menú principal
            """)

            option = int(input("> "))

            if option == 1:
                value = int(input("Ingresa un valor: "))
                self.enqueue(value)
            elif option == 2:
                self.dequeue()
            elif option == 3:
                self.get_first()
            elif option == 4:
                self.is_empty()
            elif option == 5:
                self.get_size()

