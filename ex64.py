# write a program that read many numbers inter  by the typoing 
# the prgram will sotp when 999 is typed
# In the end it shows the user the sum of all number and how many numbers where typed

sum_numbers = 0
count = 0

while True:
    num = int(input("Enter a number (999 to stop): "))
    if num == 999:
        break
    sum_numbers += num
    count += 1

print(f"Sum of all numbers: {sum_numbers}")
print(f"Total numbers entered: {count}")