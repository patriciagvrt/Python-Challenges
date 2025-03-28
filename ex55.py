# Create a program that reads the weight of five people.
# At the end, show which was the highest and the lowest weight recorded.

def calculate_weight():

    highest = 0
    lowest = 0

    for _ in range(5):
        weight = float(input('Type the weight value(Kg):  '))
        if weight > highest:
            highest = weight
            lowest = weight
        elif weight < highest:
            lowest = weight
            if weight < lowest:
                lowest = weight
                
    print(f'The highest value is {highest} the lowest value is {lowest}')

calculate_weight()