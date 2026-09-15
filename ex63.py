# Program read number n and show the n numbers of fibonacci sequence

def fi():
    n = int(input('Type a number: '))
    a, b = 0, 1
    count = 1
    while count <= n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    
    print()  # Print a newline at the end
fi()