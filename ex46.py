# Create a program that displays a countdown on the screen for a fireworks show,
# counting from 10 to 0 with a 1-second pause between each number.
from time import sleep
def fireworks():
    for i in range(10, -1, -1):
        print(f'{i}!')
        sleep(1)
    print('BOOM!')
fireworks()

