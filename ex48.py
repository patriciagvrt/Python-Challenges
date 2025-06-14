# Create a program that calculates the sum of all odd numbers that are multiples of three 
# and are found in the range from 1 to 500.

def sum_odd_three():
    s = 0
    for i in range (1, 500, 2):
        if i % 3 == 0:
            s += i
    print(f'The sum of all odd numbers that are multiples of 3 between 1 and 500 is: {s}')
sum_odd_three()

