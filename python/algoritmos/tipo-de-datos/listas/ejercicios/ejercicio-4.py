# Crea una lista de números enteros

numeros = [1, 2, 3, 4, 5]

# Pide al usuario que ingrese un número para buscar en la lista

numero = int(input("Ingresa un número: "))

# Implementa una función de búsqueda lineal que maneje el caso en el que el elemento no se encuentra en la lista 

def busqueda_lineal(numeros, numero):
    encontrado = False
    for i in range(len(numeros)):
        if numeros[i] == numero:
            encontrado = True
            break
    return encontrado

print("\nEl número está en la lista" if busqueda_lineal(numeros, numero) else "\nEl número no está en la lista")

