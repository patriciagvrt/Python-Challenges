# Create a program that read a number and show its factorial. 
def factorial():
    n =int (input('Enter a number to calculate its factorial: '))


    result = 1
    while n > 0:
        result = result * n
        n -= 1

    print(f'The factorial is {result}')

factorial()
    