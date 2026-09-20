# Create a program that read manu numbers inter
#  at the end show the medium between all of ht
# and the great and the small number typed
# The program should ask if the user wants to continue or not

sum_numbers = count = great = small = 0
num = int(input('Type a number: ')) 
conti = 'yes'
great = num 
small = num
while conti == 'yes':
    sum_numbers += num

    count += 1


    if num > great:
        great = num
    if num < small:
        small = num
    conti = str(input('Do you want to continue? [yes/no] ')).lower()
    if conti == 'no':
        break
    num = int(input('Type a number: '))
    
print (f'You typed {count} numbers and the sum of all of them is {sum_numbers}.')
print(f'The medium of the numbers is {sum_numbers / count}.')
print(f'The great number typed was {great} and the small number typed was {small}.')

