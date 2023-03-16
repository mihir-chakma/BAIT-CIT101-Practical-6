'''
Write a program to input three numbers and display the largest. (Validations required)
(PToC = 5 minutes)

'''
import sys

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

valid_number = 0 < num1 < num2 < num3

if not valid_number:
    print("Invalid input! Please enter a valid number.")
    sys.exit()

largest = num1 

if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"The largest of the three numbers is {largest}")


# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3
