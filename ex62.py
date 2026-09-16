from time import sleep

def AP():
    first = int(input("Enter the first term of the arithmetic progression: "))
    diff = int(input("Enter the common difference: "))

    terms = 10
    total = 0

    while terms != 0:
        n = 1
        while n <= terms:
            print(first, end=" ")
            first = first + diff
            n = n + 1
            total = total + 1
            sleep(0.5)

        print()
        terms = int(input(
            "How many terms would you like to see next? "
            "(Type 0 to exit): "
        ))

    print(f"Program finished. A total of {total} terms were shown.")


AP()
