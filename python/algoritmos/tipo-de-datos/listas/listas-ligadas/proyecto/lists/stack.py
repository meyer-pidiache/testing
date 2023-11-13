from lists.nodes import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.size += 1

    def pop(self):
        if self.top is None:
            print("La pila está vacía")
        else:
            removed_node = self.top
            self.top = self.top.next
            self.size -= 1
            print(f"Valor removido: {removed_node.value}")

    def peek(self):
        if self.top == None:
            print("La pila está vacía")
        else:
            print(f"Valor actual: {self.top.value}")

    def is_empty(self):
        if self.top == None:
            print("La pila está vacía")
        else:
            print("La pila no está vacía")

    def get_size(self):
        print(f"Tamaño de la pila: {self.size}")

    def menu(self):
        option = 0
        while option != 6:
            print("""
            PILA

            Seleccione una opción:
                1) Apilar
                2) Desapilar
                3) Mostrar cima
                4) ¿Está vacía?
                5) Mostrar tamaño
                6) Menú principal
            """)
            option = int(input("> "))

            if option == 1:
                value = int(input("Ingresa un valor: "))
                self.push(value)
            elif option == 2:
                self.pop()
            elif option == 3:
                self.peek()
            elif option == 4:
                self.is_empty()
            elif option == 5:
                self.get_size()

