# Create a program that makes the computer play Rock, Paper, Scissors with you.
from random import choice


def game():
    print("=" * 30)
    print("Let's play Rock, Paper, Scissors!")
    print("=" * 30)

    user_choice = input("Rock, Paper, or Scissors? ").capitalize()
    options = ["Rock", "Paper", "Scissors"]
    
    if user_choice not in options:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return

    pc_choice = choice(options)

    print(f"\nYou chose {user_choice}, and I chose {pc_choice}.")

    if pc_choice == user_choice:
        print("It's a tie!")
    elif (pc_choice == "Scissors" and user_choice == "Paper") or \
         (pc_choice == "Rock" and user_choice == "Scissors") or \
         (pc_choice == "Paper" and user_choice == "Rock"):
        print("I won!")
    else:
        print("You won!")

# Run the game
game()
