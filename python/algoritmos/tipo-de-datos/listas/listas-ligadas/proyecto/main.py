from lists.linkedList import LinkedList
from lists.doublyLinkedList import DoublyLinkedList
from lists.stack import Stack
from lists.queue import Queue

def mainMenu():
    print("""
        MENÚ PRINCIPAL

        Seleccione el tipo de estructura a usar:
            1) Lista enlazada simple
            2) Lista enlazada doble
            3) Pila
            4) Cola
            5) Salir
    """)

    option = int(input("> "))

    return option


def main():
    option = 0
    while option != 5:
        option = mainMenu()

        if option == 1:
            list = LinkedList()
            list.menu()
        elif option == 2:
            list = DoublyLinkedList()
            list.menu()
        elif option == 3:
            stack = Stack()
            stack.menu()
        elif option == 4:
            queue = Queue()
            queue.menu()

if __name__ == "__main__":
    main()

