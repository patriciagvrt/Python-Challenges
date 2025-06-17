# Redo CHALLENGE 009, displaying the multiplication table of a number chosen by the user,
# but this time using a for loop.
from time import sleep
def table_number():
    n = int(input('Chose a number for the multiplication table: '))
    for i in range(1, 11, 1):
        sleep(0.2)
        print(f'{n} x {i} = {n*i}')
table_number()

