'''
Write a program to input the radii of two coaxial circles radius_a and radius_b 
where radius_a > radius_b and display the area enclosed by them in sq. units 
using appropriate output formats in Python.

Terminology: Coaxial circles mean circles having the same centre
'''

import math

# Input the radii of the two coaxial circles
radius_a = float(input("Input the radius of the circle a: "))
radius_b = float(input("Input the radius of the circle b: "))

# Calculate the area of the two circles
area_a = math.pi * radius_a ** 2
area_b = math.pi * radius_b ** 2

# Calculate the area enclosed by the two circles
area_enclosed = area_a - area_b

# Display the area enclosed by the two circles
if radius_a > radius_b:
    print(f"The area enclosed by the two circles is: {area_enclosed:.2f} sq. units")



