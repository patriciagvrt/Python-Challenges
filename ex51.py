# Develop a program that reads the first term and the common difference of an arithmetic progression (AP).
# In the end, display the first 10 terms of this progression.

from time import sleep

def AP():
    first = int(input("Enter the first term of the arithmetic progression: "))
    diff = int(input("Enter the common difference: "))

    print("\nThe first 10 terms of the AP are:")
    for _ in range(10):
        sleep(0.2)
        print(f"{first}", end=' ')
        first += diff

AP()
