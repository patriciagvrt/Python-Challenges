# Develop a program that reads a person's weight and height, calculates their BMI,
# and displays their status according to the table below:
#
# - Below 18.5: Underweight
# - Between 18.5 and 25: Ideal weight
# - Between 25 and 30: Overweight
# - Between 30 and 40: Obesity
# - Above 40: Morbid obesity
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Classify BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Ideal weight"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
elif 30 <= bmi <= 39.9:
    category = "Obesity"
else:
    category = "Morbid obesity"

print(f"Your BMI is {bmi:.2f}. Classification: {category}.")
