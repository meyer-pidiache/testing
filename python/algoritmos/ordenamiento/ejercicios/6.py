"""
Utiliza el algoritmo de mezcla (merge sort) para ordenar la siguiente lista de números en orden ascendente: [34, 12, 5, 2, 45, 1, 33, 7]
"""

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

numbers = [34, 12, 5, 2, 45, 1, 33, 7]

print(merge_sort(numbers))

