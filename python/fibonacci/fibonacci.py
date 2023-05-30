position = int(input("Type Fibonacci Lenght: "))


def getFibonacci(number) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return getFibonacci(number - 2) + getFibonacci(number - 1)


def getByRecursion(position) -> list:
    sequence = list()
    for i in range(position):
        sequence.append(getFibonacci(i))

    return sequence

def getByLineal(position) -> list:
    sequence = list()

    less2, less1 = 0, 1

    if position == 0:
        return [less2]
    elif position == 1:
        return [less2, less1]
    else:
        sequence = [less2, less1]
        for _ in range(2, position):
            new = less2 + less1
            sequence.append(new)

            less2 = less1
            less1 = new

        return sequence

def main() -> None:
    if position > 30:
        print("\n", getByLineal(position))
        print("\nLineal mode implement")
    else:
        print("\n", getByRecursion(position))
        print("\nRecursion mode implement")

if __name__ == "__main__":
    main()
