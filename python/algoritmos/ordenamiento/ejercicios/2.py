"
2. Utiliza el algoritmo de burbuja para ordenar la siguiente lista de palabras en orden alfabético {'manzana', 'banana', 'fresa', 'Mora', 'kiwi}
"

fruits= ['manzana', 'banana', 'fresa', 'mora', 'kiwi']
print(sorted(fruits))

def bubbleSort(fruits):
    counter = len(fruits) - 1
    for i in range(len(fruits)-1):
        for j in range(counter):
            if fruits[j] > fruits[j+1]:
                fruit = fruits[j+1]
                fruits[j+1] = fruits[j]
                fruits[j] = fruit 
        counter -= 1

bubbleSort(fruits)
print(fruits)
