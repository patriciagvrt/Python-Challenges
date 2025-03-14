# Guessing Game  
# The user tries to guess the number the machine is thinking of.  

import random
from time import sleep

def lotto(x):
    sort_guess = random.randint(1, 5) 
    if x == sort_guess:
        print(f'You won! I was thinking of the number {sort_guess}.')
    else:
        print(f'You lost! I was thinking of the number {sort_guess}.')

print('=*' * 20)
print("I'm going to think of a number from 1 to 5. Can you guess?")
print('=*' * 20)    

user_guess = int(input('What number did I think of? ')) 
print('Processing...')
sleep(2)

lotto(user_guess)

