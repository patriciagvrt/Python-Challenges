# Search for a substring within a string.  
# Ask for the full name and verify if the person has the surname "Smith".
def surname(n):
    print(f'Does your name has the surname Smith? {"SMITH" in n}')
name = str(input('Whats your full name? ')).strip().upper()
surname(name)