# redo the 51 challenge reading the first number
# and the common difference of a arithmetic progression
# showing the 10 first terms of this progression using a while loop.
from time import sleep
def AP():
    first = int(input('Enter the first term of the arithmetic progression: '))
    diff = int(input('Enter the common difference: '))
    n = 1
    while n <11:
        print(f'{first}', end=' ')
        first += diff
        n += 1
        sleep(0.5)
AP()