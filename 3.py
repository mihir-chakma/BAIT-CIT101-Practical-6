'''
Write a program to input three numbers and display the largest. (Validations required)
(PToC = 5 minutes)

'''
import sys

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if not num1 > 0:
    print("Invalid input! Please enter a valid number.")
    sys.exit()

if not num2 > 0:
    print("Invalid input! Please enter a valid number.")
    sys.exit()

if not num3 > 0:
    print("Invalid input! Please enter a valid number.")
    sys.exit()

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is : {largest}")


