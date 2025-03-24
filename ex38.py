# Write a program that reads two integer numbers and compares them,
# displaying a message on the screen:
#
# - "The first value is greater" if the first number is larger.
# - "The second value is greater" if the second number is larger.
# - "There is no greater value, both are equal" if the numbers are the same.
def greater_value():
    n1 = int(input('Type the first number: '))
    n2 = int(input('Type the second number: '))
    if n1 > n2:
        print('The first value is greater')
    elif n2 > n1:
        print('The second value is greater')
    else:
        print(f'The two values are equal')
greater_value()
    