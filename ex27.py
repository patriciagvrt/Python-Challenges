# Extract first and last name from the user's full name  
# The user inputs their full name, and the program returns their first and last name.  

def name(x):
    print(f'Nice to meet you, {x}!')
    separated = x.split()
    print(f'Your first name is {separated[0]}.')
    print(f'Your last name is {separated[-1]}.')

# Get user input
n = str(input('Type your full name: ')).strip()
name(n)