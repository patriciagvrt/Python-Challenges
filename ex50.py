# Develop a program that reads six integers and shows the sum of only those that are even.
# If the entered value is odd, ignore it.

def sum_even():
    s = 0
    for i in range(1, 7):
        n = int(input(f'Enter the {i}ᵗʰ number: '))
        if n % 2 == 0:
            s += n
    print(f'\nThe sum of all even numbers entered is: {s}')

sum_even()
