# Guessing game
# User try to guess the number the machine tough

import random
from time import sleep
def lotto(x):
    sort_guess = random.randrange(1, 5)
    if x == sort_guess:
        print(f'You won I was thinking the number {sort_guess}')
    else:
        print(f'You lost I was thinking the number {sort_guess}')

print('=*'*20)
print('Im going to think of a number from 1 to 5. Can you guess?')
print('=*'*20)    
user_guess = int(input('What number did i think off? '))
print('Processing...')
sleep(2)

lotto(user_guess)
