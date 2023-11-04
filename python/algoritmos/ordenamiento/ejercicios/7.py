"""
Ordena los números pares de la siguiente lista en orden ascendente: [7, 12, 3, 8, 14, 6, 9, 10]
"""

def sort_even_numbers(array):
   indexes = [i for i in range(len(array)) if array[i] % 2 == 0] 
   odd_sorted = sorted(array[i] for i in indexes)

   for i in range(len(array)):
       print(i)
       if i in indexes:
           array[i] = odd_sorted[0]
           odd_sorted.pop(0)

   return array

numbers = [7, 12, 3, 8, 14, 6, 9, 10]

print(numbers)
print(sort_even_numbers(numbers))

