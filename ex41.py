# The National Swimming Confederation needs a program that reads an athlete's birth year
# and displays their category based on age:
#
# - Up to 9 years old: MIRIM
# - Up to 14 years old: INFANTIL
# - Up to 19 years old: JUNIOR
# - Up to 20 years old: SENIOR
# - Above 20 years old: MASTER

from datetime import date

def categorize_athlete():
    current_year = date.today().year
    birth_year = int(input("Type your birth year: "))
    age = current_year - birth_year

    if age > 20:
        print(f"You are {age} years old. Your category is MASTER.")
    elif age == 20:
        print(f"You are {age} years old. Your category is SENIOR.")
    elif 15 <= age <= 19:
        print(f"You are {age} years old. Your category is JUNIOR.")
    elif 10 <= age <= 14:
        print(f"You are {age} years old. Your category is INFANTIL.")
    else:
        print(f"You are {age} years old. Your category is MIRIM.")

# Call the function
categorize_athlete()



