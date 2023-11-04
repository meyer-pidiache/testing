"""
3. Ordena los siguientes números en orden descendente utilizando el algoritmo de inserción: [12, 45, 3, 7, 1, 21, 10]
"""

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array

numbers = [12, 45, 3, 7, 1, 21, 10]

print(insertion_sort(numbers))

