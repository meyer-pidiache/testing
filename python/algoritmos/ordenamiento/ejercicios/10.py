"""
Utiliza el algoritmo de selección para ordenar los siguientes números en orden descendente: [20, 15, 30, 10, 5, 25]
"""

def reverse_selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] > array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array

numbers = [20, 15, 30, 10, 5, 25]

print(reverse_selection_sort(numbers))

