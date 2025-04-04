# Redo CHALLENGE 035 about triangles, adding the feature to display the type of triangle formed:
# Use functions
# - Equilateral: all sides are equal
# - Isosceles: two sides are equal
# - Scalene: all sides are different

def triangle_type(a, b, c):
    if a == b == c:
        print("This triangle is an equilateral triangle.")
    elif a == b or a == c or b == c:
        print("This triangle is an isosceles triangle.")
    else: 
        print("This triangle is a scalene triangle.")

def triangle_form(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("You can form a triangle!")
        triangle_type(a, b, c)
    else:
        print("You cannot form a triangle.")

# Get user input
print("Enter three segment lengths, and I will tell you if they can form a triangle.")
x = float(input("Type the first line segment: "))
y = float(input("Type the second line segment: "))
z = float(input("Type the third line segment: "))

# Call function
triangle_form(x, y, z)
   


   