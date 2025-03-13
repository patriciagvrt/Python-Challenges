# Guessing game
# User try to guess the number the machine tough

import random
def lotto(x):

    sort_guess = random.randrange(1, 5)
    if x == sort_guess:
        print(f'You won i think of the number {sort_guess}')
    else:
        print(f'You lost i think of th enumber {sort_guess}')

print('=*'*20)
print('Im going to think of a number from 1 to 5. Can you guess?')
print('=*'*20)    
user_guess = int(input('What number did i think off? '))
lotto(user_guess)
