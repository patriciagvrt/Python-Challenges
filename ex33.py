# Create a program that reads three numbers and displays which one is the largest and which one is the smallest

def analyzer(x, y, z):
    # Finding the smallest number
    if x <= y and x <= z:
        smallest = x
    elif y <= x and y <= z:
        smallest = y
    else:
        smallest = z

    # Finding the largest number
    if x >= y and x >= z:
        largest = x   
    elif y >= x and y >= z:
        largest = y
    else:
        largest = z

    print(f'The largest number is {largest}.')
    print(f'The smallest number is {smallest}.')

# Get user input
n1 = int(input('Type the first number: '))
n2 = int(input('Type the second number: '))
n3 = int(input('Type the third number: '))

analyzer(n1, n2, n3)
