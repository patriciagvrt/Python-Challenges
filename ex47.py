# Create a program that displays all even numbers between 1 and 50.
from time import sleep

def even_number():
    for i in range(2, 51, 2):  # Start at 2, go up to 50, step by 2
        sleep(0.1)
        print(f'{i}', end=' ')
    
even_number()
