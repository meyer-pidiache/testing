# Búsqueda binaria en una lista ordenada para encontrar un número específico.

# Lista ordenada de números.
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# El número a buscar.
numero_a_buscar = 100

def buscador_binario(numeros, numero_a_buscar):
    # Busca el número en la lista.
    izq = 0
    der = len(numeros) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if numeros[medio] == numero_a_buscar:
            return medio + 1
        elif numeros[medio] < numero_a_buscar:
            izq = medio + 1
        else:
            der = medio - 1

print(f"El número {numero_a_buscar} se encuentra en la posición: {buscador_binario(numeros, numero_a_buscar)}")

