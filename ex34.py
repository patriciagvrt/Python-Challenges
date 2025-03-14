# Write a program that asks for an employee's salary and calculates the amount of their raise.
# For salaries greater than R$1,250.00, apply a 10% raise.
# For salaries equal to or lower than this amount, apply a 15% raise.

def raise_salary(salary):
    if salary > 1250:
        new_salary = salary + (salary * 0.10)
        print(f'You will get a 10% raise, increasing your salary to ${new_salary:.2f}.') 
    else:
        new_salary = salary + (salary * 0.15)
        print(f'You will get a 15% raise, increasing your salary to ${new_salary:.2f}.')   

# Get user input:
salary = float(input("What's your salary? "))
raise_salary(salary)
