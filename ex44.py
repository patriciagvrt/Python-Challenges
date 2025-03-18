# Create a program that calculates the final price of a product based on its normal price
# and the payment method chosen:
#
# - Paying in cash/check: 10% discount
# - Paying in full with a card: 5% discount
# - Up to 2x on the card: normal price
# - 3x or more on the card: 20% interest

def final_price(normal_price, payment_method):
    if payment_method == '1':
        new_price = normal_price - (normal_price * 0.10)
        print(f"Your final price with a 10% discount is ${new_price:.2f}")
    elif payment_method == '2':
        new_price = normal_price - (normal_price * 0.05)
        print(f"Your final price with a 5% discount is ${new_price:.2f}")    
    elif payment_method == '3':
        print(f"Your final price is ${normal_price:.2f}")
    elif payment_method == '4':
        new_price = normal_price + (normal_price * 0.20)
        print(f"Your final price with a 20% interest is ${new_price:.2f}")
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

# Get user input
normal_price = float(input("Type the price of the product: $ "))
payment_method = input(
    "Choose a payment method:\n"
    " 1 - Cash/check (10% discount)\n"
    " 2 - Full card (5% discount)\n"
    " 3 - 2x on the card (normal price)\n"
    " 4 - 3x or more on the card (20% interest)\n"
    "Choice: "
)

# Call function with parameters
final_price(normal_price, payment_method)
