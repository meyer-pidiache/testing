"Búsqueda de cadenas de texto"

# Crea una lista de nombres

nombres = ["juan", "pedro", "lucía"]

# Pide al usuario que ingrese un nombre para buscar en la lista

nombre = input("Ingresa un nombre: ").lower()

# Implementa una función de búsqueda lineal que ignore mayúsculas/minúsculas y muestre si el nombre está en la lista

def busqueda_lineal(nombres, nombre):
    encontrado = False
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            encontrado = True
            break
    return encontrado

print(f"\nEl nombre está en la lista" if busqueda_lineal(nombres, nombre) else "\nEl nombre no está en la lista")

