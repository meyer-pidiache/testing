from lists.nodes import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                print("El valor se encuentra en la lista")
                return
            current = current.next
        print("El valor no se encuentra en la lista")

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            print(f"Se ha eliminado el valor {value}")
            return
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                print(f"Se ha eliminado el valor {value}")
                return
            current = current.next

        print(f"El valor {value} no se encuentra en la lista")

    def show(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None\n")

    def menu(self):
        option = 0
        while option != 5:
            print("""
            LISTA ENLAZADA SIMPLE

            Seleccione una opción:
                1) Agregar valor
                2) Buscar valor
                3) Eliminar valor
                4) Mostrar lista
                5) Menú principal
            """)

            option = int(input("> "))

            if option == 1:
                value = int(input("Valor a agregar: "))
                self.append(value)
            elif option == 2:
                value = int(input("Valor a buscar: "))
                self.find(value)
            elif option == 3:
                value = int(input("Valor a eliminar: "))
                self.delete(value)
            elif option == 4:
                self.show()

