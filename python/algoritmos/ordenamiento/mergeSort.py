'''
El algoritmo de ordenamiento Merge Sort es un enfoque basado en la técnica "dividir y conquistar" para organizar un conjunto de elementos. Su lógica se basa en los siguientes pasos:

    División: El arreglo no ordenado se divide en dos mitades iguales. Este proceso se repite recursivamente hasta que se obtienen subarreglos de tamaño 1 o 0, que se consideran ordenados por definición.

    Conquista: Luego, se ordenan las mitades individualmente mediante llamadas recursivas al mismo algoritmo. Esto implica que cada mitad se divide nuevamente en dos mitades, y el proceso continúa hasta que todas las subdivisiones estén ordenadas.

    Combinación: Una vez que todas las mitades están ordenadas, se combinan de manera eficiente en un solo arreglo ordenado. Para lograr esto, se compara el primer elemento de cada mitad y se selecciona el más pequeño para agregarlo al arreglo resultante. Este proceso de comparación y combinación se repite hasta que ambas mitades se hayan agotado y se hayan unido.

Merge Sort garantiza que las dos mitades se combinen en orden, lo que finalmente resulta en un arreglo ordenado. Debido a su eficiencia y su rendimiento constante en términos de tiempo (O(n log n)), Merge Sort es una opción popular para ordenar arreglos, especialmente en aplicaciones en las que se requiere estabilidad en el ordenamiento.
'''
def merge_sort(arr):
    # Verificamos si la longitud del arreglo es 1 o 0, en cuyo caso ya está ordenado.
    if len(arr) <= 1:
        return arr
    
    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
   
    # Llamamos recursivamente a merge_sort en las dos mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinar las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    # Combinar las dos mitades ordenadas en un solo arreglo ordenado
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Agregar cualquier elemento restante de las dos mitades
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Ejemplo de uso
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Arreglo no ordenado:", arr)
    
    sorted_arr = merge_sort(arr)
    print("Arreglo ordenado:", sorted_arr)

