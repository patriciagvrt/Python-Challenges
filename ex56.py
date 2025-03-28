# Develop a program that reads the name, age, and gender of 4 people.
# At the end of the program, display:
# - The average age of the group.
# - The name of the oldest man.
# - How many women are under 20 years old.

def signup():
    total_age = 0
    oldest_age = 0
    oldest_man_name = ''
    women_under_20 = 0

    for _ in range(4):
        name = input("Name: ").strip()
        age = int(input("Age: "))
        gender = input("Gender (M/F): ").strip().upper()

        total_age += age

        if gender == 'F' and age < 20:
            women_under_20 += 1

        if gender == 'M' and age > oldest_age:
            oldest_age = age
            oldest_man_name = name

    average_age = total_age / 4
    print(f"\nThe average age of the group is {average_age:.1f} years.")
    if oldest_man_name:
        print(f"The oldest man is {oldest_man_name}, who is {oldest_age} years old.")
    else:
        print("There were no men in the group.")
    print(f"There are {women_under_20} women under 20 years old.")

signup()
