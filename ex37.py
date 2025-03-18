# Write a program that reads any integer and asks the user to choose the base for conversion:
# - 1 for binary
# - 2 for octal
# - 3 for hexadecimal

def conversion():
    num = int(input('Enter a decimal number: '))
    choice = int(input('''\nChoose the base for conversion:
    1 - Binary
    2 - Octal
    3 - Hexadecimal
    Choice: ''')) 

    if choice == 1:
        conv = bin(num)[2:]  # Remove the "0b" prefix
        print(f'The binary version of {num} is {conv}')
    elif choice == 2:
        conv = oct(num)[2:]  # Remove the "0o" prefix
        print(f'The octal version of {num} is {conv}')
    elif choice == 3:
        conv = hex(num)[2:].upper()  # Remove "0x" and convert to uppercase
        print(f'The hexadecimal version of {num} is {conv}')
    else:
        print('Invalid choice! Please enter 1, 2, or 3.')

# Call the function
conversion()
