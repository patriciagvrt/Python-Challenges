# Create a program that reads an integer and tells whether or not it is a prime number.

def prime_number():
    n = int(input("Type a number and I'll tell you if it's a prime number or not: "))
    divisor_count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1

    if divisor_count == 2:
        print(f"\nThe number {n} is a prime number.")
    else:
        print(f"\nThe number {n} is not a prime number.")

prime_number()
