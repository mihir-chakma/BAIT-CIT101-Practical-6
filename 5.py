'''
The following criteria are used to grade the marks obtained by candidates for a subject in
an examination.

0 ≤ marks < 40 Grade = 'F'
40 ≤ marks < 55 Grade = 'S'
55 ≤ marks < 65 Grade = 'C'
65 ≤ marks < 75 Grade = 'B'
75 ≤ marks ≤ 100 Grade = 'A'

Create a Python application to enter the name and the marks obtained by a candidate for a
given subject and display the name and the grade obtained. Include suitable validations.

'''
import sys

# Input candidate details
candidate_name = input("Enter candidate name: ").capitalize()
marks = int(input("Enter marks obtained (out of 100): "))

# Validate marks input
if not marks > 0:
    print("Error: Marks should be between 0 and 100.")
    sys.exit()

# Determine grade based on marks obtained
if 0 <= marks < 40:
    grade = 'F'
elif 40 <= marks < 55:
    grade = 'S'
elif 55 <= marks < 65:
    grade = 'C'
elif 65 <= marks < 75:
    grade = 'B'
elif 75 <= marks <= 100:
    grade = 'A'

# Display candidate details and grade obtained
print(f"Candidate Name: {candidate_name}")
print(f"Marks Obtained: {marks}")
print(f"Grade: {grade}")



