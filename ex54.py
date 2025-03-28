# Create a program that reads the birth year of seven people.
# At the end, show how many of them are still minors and how many are already adults.
from datetime import date

def birthdays():
    current_year = date.today().year # get the current year from the pc

    minors = 0
    adults = 0

    for _ in range (7):
        birthyear = int(input('Type the year of birthyear: ')) # user input
        age = current_year - birthyear
        if age < 18:
            minors += 1
        else:
            adults += 1

    print(f'There are {minors} minors. And {adults} adults!')

birthdays()
