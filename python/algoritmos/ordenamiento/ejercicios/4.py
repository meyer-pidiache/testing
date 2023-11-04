"""
Aplica el algoritmo de selección para ordenar la siguiente lista de números en orden ascendente: [8, 4, 9, 2, 5, 1, 7, 6]
"""

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

numbers = [8, 4, 9, 2, 5, 1, 7, 6]

print(selection_sort(numbers))

