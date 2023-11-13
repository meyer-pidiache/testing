# Búsqueda binaria en una lista de nombres 

# Lista ordenada de nombres.

nombres = ["Ana", "Carlos", "Diana", "Eduardo", "Florencia", "Gustavo", "Hugo", "Ingrid", "Juan", "Leticia"]


# El número a buscar.
nombre_a_buscar = "Carlos" 

def buscador_binario(nombres, nombre_a_buscar):
    # Busca el número en la lista.
    izq = 0
    der = len(nombres) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if nombres[medio] == nombre_a_buscar:
            return medio + 1
        elif nombres[medio] < nombre_a_buscar:
            izq = medio + 1
        else:
            der = medio - 1

print(f"El nombre '{nombre_a_buscar}' se encuentra en la posición: {buscador_binario(nombres, nombre_a_buscar)}")

