# Create a program that reads a phrase and tells whether it is a palindrome,
# ignoring spaces.
#
# Examples:
# Was it a car or a cat I saw?
# No lemon, no melon

def palindrome():
    phrase = input('Type a phrase: ').replace(" ", "").lower()
    reversed_phrase = phrase[::-1]

    if phrase == reversed_phrase:
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")



palindrome()

