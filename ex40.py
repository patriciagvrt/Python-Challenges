# Create a program that reads two grades from a student and calculates their average.
# Display a message at the end based on the achieved average:
# - Average below 5.0: FAILED
# - Average between 5.0 and 6.9: RECOVERY
# - Average 7.0 or higher: PASSED

def average_grade():
    n1 = float(input("Enter grade 1: "))
    n2 = float(input("Enter grade 2: "))
    grade = (n1 + n2) / 2

    if grade < 5.0:
        print(f"Unfortunately, your average was {grade:.2f}. You failed.")
    elif 5.0 <= grade <= 6.9:
        print(f"Your average was {grade:.2f}. You are in recovery.")
    else:
        print(f"Congratulations! Your average was {grade:.2f}. You passed!")

# Call the function
average_grade()
