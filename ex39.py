# Write a program that reads a young person's birth year and informs them, based on their age:
#
# - If they still have time before enlisting in military service.
# - If it is time to enlist.
# - If they have already passed the enlistment period.
#   Military service age: 18 years old
#
# The program should also display the time remaining or how long it has been since the enlistment deadline.

from datetime import date

def military_service():
    current_year = date.today().year
    year_birth = int(input("What year were you born? "))
    age = current_year - year_birth  # Calculate age

    if age < 18:
        print(f"You are {age} years old. You still have {18 - age} year(s) left to enlist.")
    elif age == 18:
        print("You are 18 years old. It's time to enlist!")
    else:
        print(f"You are {age} years old. It has already been {age - 18} year(s) since you should have enlisted.")

military_service()



