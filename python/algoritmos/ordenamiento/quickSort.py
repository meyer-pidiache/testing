'''
La lógica del algoritmo de ordenamiento Quick Sort se basa en el principio de "dividir y conquistar" y se puede resumir en los siguientes pasos:

    Selección del Pivote: El algoritmo elige un elemento del arreglo como pivote. El pivote puede seleccionarse de diversas maneras, comúnmente se elige el último elemento del arreglo. El propósito del pivote es servir como punto de referencia para dividir el arreglo en tres partes: elementos menores que el pivote, iguales al pivote y mayores que el pivote.

    Particionamiento: Se recorre el arreglo y se clasifican los elementos en tres grupos distintos. Se crean tres listas: una para los elementos menores que el pivote, otra para los elementos iguales al pivote y una tercera para los elementos mayores que el pivote. Esto se logra mediante comparaciones con el pivote.

    Llamadas Recursivas: Una vez que los elementos están clasificados, se realizan llamadas recursivas en los subarreglos que contienen elementos menores y mayores que el pivote. Estos subarreglos se ordenan de la misma manera, eligiendo un pivote en cada uno y repitiendo el proceso.

    Combinación: Finalmente, se combinan los subarreglos ordenados junto con los elementos iguales al pivote para formar el arreglo completamente ordenado. Los elementos iguales al pivote ya están en su posición correcta debido al proceso de particionamiento.

El algoritmo Quick Sort es muy eficiente y tiene un rendimiento promedio de O(n log n) en comparaciones, lo que lo hace adecuado para arreglos de gran tamaño. Sin embargo, la elección del pivote puede influir en su rendimiento, por lo que existen variaciones del algoritmo que utilizan estrategias más sofisticadas para seleccionar el pivote, como el pivote mediano de tres o el pivote aleatorio. La clave para el éxito del Quick Sort radica en el particionamiento eficiente y la elección inteligente del pivote.
'''
def quick_sort(arr):
    # Caso base: Si el arreglo tiene 0 o 1 elemento, ya está ordenado.
    if len(arr) <= 1:
        return arr

    # Elegir un elemento pivote (por ejemplo, el último elemento)
    pivot = arr[-1]

    # Inicializar listas para los elementos menores, iguales y mayores que el pivote
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    # Particionar los elementos en las tres listas según su relación con el pivote
    for element in arr:
        if element < pivot:
            less_than_pivot.append(element)
        elif element == pivot:
            equal_to_pivot.append(element)
        else:
            greater_than_pivot.append(element)

    # Llamadas recursivas en las dos sub-listas (menores y mayores que el pivote)
    sorted_less = quick_sort(less_than_pivot)
    sorted_greater = quick_sort(greater_than_pivot)

    # Combinar las tres listas ordenadas
    return sorted_less + equal_to_pivot + sorted_greater

# Ejemplo de uso
if __name__ == '__main__':
    arr = [12, 4, 5, 6, 7, 3, 1, 15, 2, 8]
    print("Arreglo no ordenado:", arr)
    
    sorted_arr = quick_sort(arr)
    print("Arreglo ordenado:", sorted_arr)
