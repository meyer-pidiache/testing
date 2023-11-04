'''
El algoritmo Cocktail Sort es una variante del algoritmo de burbuja (Bubble Sort) que realiza múltiples pasadas a través del arreglo, primero moviendo el elemento más grande hacia el final y luego el elemento más pequeño hacia el principio en cada pasada. Este proceso se repite hasta que no se realicen intercambios en una pasada completa, lo que indica que el arreglo está ordenado. El algoritmo se llama "Cocktail Sort" debido a la idea de "mezclar" los elementos en el arreglo, moviendo el más grande y el más pequeño en direcciones opuestas.
'''
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    
    while (swapped == True):
        # Reseteamos la bandera swapped en cada pasada
        swapped = False
        
        # Llevamos el elemento más grande al final
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # Si no se realizó ningún intercambio, el arreglo ya está ordenado
        if (swapped == False):
            break
        
        swapped = False
        
        # Movemos el elemento más pequeño al principio
        end = end - 1
        
        for i in range(end - 1, start - 1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # Aumentamos el índice del inicio
        start = start + 1

# Ejemplo de uso
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Arreglo no ordenado:", arr)
    
    cocktail_sort(arr)
    print("Arreglo ordenado:", arr)
