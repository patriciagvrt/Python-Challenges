# First and last occurrence of a letter
# The user enters a phrase, and the program counts how many times the letter 'A' appears and in what positions it appears first and last.
def letter_A(x):
    print(f'The letter A appears {x.count("A")} times in the phrase')
    print(f'The first time the letter A appear was in the {x.find("A") + 1} positon')
    print(f'The last time the letter A appear was in the {x.rfind("A")+1} postion')
# get user input
phrase = str(input('Type a phrase: ')).strip().upper()
letter_A(phrase)