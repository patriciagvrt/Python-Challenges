# Create a program that reads a year and determines whether it is a leap year.
def leapyear(x):
    if x % 4 == 0 and x % 100 != 0:
        print(f'The year {x} is a leap year!')
    else:
        print(f'The year {x} is not a leap year')
year = int(input('Type a year: '))
leapyear(year)
