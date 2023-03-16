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
marks_obtained = float(input("Enter marks obtained (out of 100): "))

# Validate marks input
if not marks_obtained < 0 or marks_obtained > 100:
    print("Error: Marks should be between 0 and 100.")
    sys.exit()

# Determine grade based on marks obtained
if marks_obtained < 40:
    grade = 'F'
elif marks_obtained < 55:
    grade = 'S'
elif marks_obtained < 65:
    grade = 'C'
elif marks_obtained < 75:
    grade = 'B'
else:
    grade = 'A'

# Display candidate details and grade obtained
print("Candidate Name:", candidate_name)
print("Marks Obtained:", marks_obtained)
print("Grade:", grade)


# import sys
# name = input("Enter your name : ")
# marks = int(input("Enter marks : "))
# invalid = 0 < marks
# if not invalid:
#     print("Invalid input! Please enter a valid number.")
#     sys.exit()
# if 100 <= marks and  75 >= marks:
#     result = "A"
# print(result)
