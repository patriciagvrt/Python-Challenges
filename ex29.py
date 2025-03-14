# SPEED CAMERA  
# Checks if the vehicle exceeded the speed limit and calculates the fine if necessary.  

def speed_cam(speed):
    if speed > 80:
        print('Ticket! You exceeded the speed limit of 80 km/h.')
        ticket = (speed - 80) * 7
        print(f'Your ticket fine is ${ticket:.2f}.')
    else:
        print('You are within the speed limit. Drive safely!')

# Get user input  
speed = int(input('What was the speed of the vehicle? '))
speed_cam(speed)
