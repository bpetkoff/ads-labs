
# Task 3 - Lucky numbers
#
chosen_number = input("Please enter your number: ")

with open("lucky ids.txt", "r") as f:
    numbers = f.read()
list_numbers = numbers.split('\n')
if chosen_number in list_numbers:
    print("Yes - your id is listed")
else:
    print("No - your id is NOT listed")
