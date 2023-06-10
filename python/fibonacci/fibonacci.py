position = int(input("Type Fibonacci Lenght: "))

def getFibonacci(number) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        a = getFibonacci(number - 2)
        b = getFibonacci(number - 1)
        return a + b

def getByRecursion(position) -> list:
    sequence = list()
    for i in range(position):
        sequence.append(getFibonacci(i))

    return sequence

def getByLineal(position) -> list:
    sequence = list()

    less2, less1 = 0, 1

    sequence = [less2, less1]
    for _ in range(2, position):
        new_v = less2 + less1
        sequence.append(new_v)

        less2 = less1
        less1 = new_v

    return sequence

def main() -> None:
    if position > 15:
        print("\n", getByLineal(position))
        print("\nLineal mode implement")
    else:
        print("\n", getByRecursion(position))
        print("\nRecursion mode implement")

if __name__ == "__main__":
    main()
