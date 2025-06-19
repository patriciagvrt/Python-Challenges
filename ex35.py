# Develop a program that reads the lengths of three line segments 
# and tells the user whether they can form a triangle or not. Use only if 

def triangle_form(a, b, c):
    if a + b > c:
        if a + c > b:
            if b + c > a:
                print('You can form a triangle!')
            else:
                print('You cannot form a triangle.')
        else:
            print('You cannot form a triangle.')
    else:
        print('You cannot form a triangle.')

print('Tell me three segment lengths, and I will tell you if they can form a triangle.')
x = float(input('Type the first line segment: '))
y = float(input('Type the second line segment: '))
z = float(input('Type the third line segment: '))
triangle_form(x, y, z)


