# Create a program that read two values and show 
# a menu on the screen:
# [1] Sum
# [2] Multiply
# [3] Find the greater
# [4] Enter new numbers
# [5] Exit the program
# the program must perform the operation requested in the menu.

global num1, num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def menu(num1, num2):
    while True:
        print("Menu:")
        print("[1] Sum")
        print("[2] Multiply")
        print("[3] Find the greater")
        print("[4] Enter new numbers")
        print("[5] Exit the program")

        choice = input("Choose an option: ")

        if choice == '1':
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is: {result}")
        elif choice == '2':
            result = num1 * num2
            print(f"The product of {num1} and {num2} is: {result}")
        elif choice == '3':
            greater = max(num1, num2)
            print(f"The greater number between {num1} and {num2} is: {greater}")
        elif choice == '4':

            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid option from the menu.")
menu(num1, num2)