# Create a program that reads an integer and displays on the screen whether it is EVEN or ODD.

def analyze(x):
    if x % 2 == 0:
        print(f'{x} is an even number!')
    else:
        print(f'{x} is an odd number!')

num = int(input('Tell me a number, and I will tell you if it is an odd or even number: '))
analyze(num)
