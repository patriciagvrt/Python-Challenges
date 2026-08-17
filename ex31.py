# Develop a program that asks for the distance of a trip in kilometers.
# Calculate the ticket price, charging R$0.50 per km for trips up to 200 km and R$0.45 for longer trips.

def analyze(distance):
    if distance <= 200:
        price = 0.50 * distance
    else:
        price = 0.45 * distance
        
    print(f'You traveled {distance} kilometers, so your total fare will be R${price:.2f}.')

# Get user input
distance = int(input('What distance did you travel? '))
analyze(distance)


