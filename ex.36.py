# Write a program to approve a bank loan for purchasing a house.
# The program will ask for the house price, the buyer's salary, and the number of years they will take to pay it off.
# Calculate the monthly installment amount, ensuring that it does not exceed 30% of the buyer's salary.
# If it does, the loan will be denied.

def approve_loan():
    house_price = float(input('What is the full price of the house? $'))
    buyers_salary = float(input('What is your salary? $'))
    number_years = int(input('How many years will you take to pay it off? '))

    number_months = number_years * 12  # Total number of months
    monthly_installment = house_price / number_months  # Monthly payment
    max_allowed = buyers_salary * 0.30  # 30% of the buyer's salary

    print(f'\nThe monthly installment will be: ${monthly_installment:.2f}')
    
    if monthly_installment <= max_allowed:
        print('Congratulations! Your loan has been approved.')
    else:
        print('Sorry, your loan was not approved.')

# Run the function
approve_loan()
