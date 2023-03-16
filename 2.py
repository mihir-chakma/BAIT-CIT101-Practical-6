'''
Write a program to enter the length L (in meters) of a simple pendulum and find its period (T in seconds) 
assuming that the gravitational acceleration is 9.834 m/s-2. 

Hint: Use the formula T = 2sqrt(L/g)
(PToC = 5 minutes)

'''

import math

# Input the length of the simple pendulum
length = float(input("Enter the length of the pendulum (in meters): "))

# Calculate the period of the simple pendulum
g = 9.834 # acceleration due to gravity in m/s^2
period = 2 * math.pi * math.sqrt(length / g)

# Display the period of the simple pendulum
print("The period of the pendulum is: {:.2f} seconds".format(period))


"""
In this program, we first import the math module to use the value of pi and the sqrt() function. 
We then input the length of the simple pendulum from the user. 
We calculate the period of the simple pendulum using the formula T = 2*pi*sqrt(L/g), 
where L is the length of the pendulum and g is the acceleration due to gravity. 
We use the value of g as 9.834 m/s^2, as given in the problem statement. Finally, 
we display the period of the simple pendulum using the print() function and formatting 
the output to two decimal places using the :.2f format specifier.
"""
