# Create a program that reads a year and determines whether it is a leap year.
from datetime import date
def leapyear(x):
    if x == 0:
       x = date.today().year
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print(f'The year {x} is a leap year!')
    else:
        print(f'The year {x} is not a leap year')
year = int(input('Type a year, type 0 if you want the current year: '))
leapyear(year)
