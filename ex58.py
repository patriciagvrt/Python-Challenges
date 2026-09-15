import random
from time import sleep

def lotto():
    secret_number = random.randint(1, 10)

    print("=*" * 20)
    print("I'm going to think of a number from 1 to 10. Can you guess?")
    print("=*" * 20)

    while True:
        try:
            user_guess = int(input("What number did I think of? "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if user_guess < 1 or user_guess > 10:
            print("Please enter a number from 1 to 10.")
            continue

        print("Processing...")
        sleep(1)

        if user_guess == secret_number:
            print(f"You won! I was thinking of the number {secret_number}.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


lotto()