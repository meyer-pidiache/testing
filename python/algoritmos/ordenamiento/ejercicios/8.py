"""
Aplica el algoritmo de burbuja mejorado (con bandera) para ordenar la siguiente lista en orden ascendente: [5, 1, 4, 2, 8, 7, 3, 6]
"""

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Se establece una bandera para verificar si se realizó algún intercambio en la pasada actual
        intercambio = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Se intercambian los elementos si están en orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
        # Si no hubo intercambios en la pasada actual, la lista está ordenada y se termina el bucle
        if not intercambio:
            print("La lista esta ordenada")
            break
    return lista

numbers = [5, 1, 4, 2, 8, 7, 3, 6]

print(bubble_sort(numbers))
