"Encontrar elementos múltiples"

# Crea una lista con elementos repetidos

numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Solicita al usuario que ingrese un número para buscar en la lista

numero = int(input("Ingresa un número: "))

# Implementa una función de búsqueda lineal para encontrar todas las ocurrencias del número y mostrar sus índices

def busqueda_lineal(numeros, numero):
    indices = []
    for i in range(len(numeros)):
        if numeros[i] == numero:
            indices.append(i)
    return indices

print(f"\nEl número está en los índices: {busqueda_lineal(numeros, numero)}")

