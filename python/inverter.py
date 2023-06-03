numero = int(input("Ingresa un número de 4 dígitos: "))

for _ in range(4):
    print(numero%10, end='')
    numero = numero // 10
