'''
A company decides to give a New Year bonus to its employees. Their policy is such that a male
worker would get 5% of the salary while a female worker would get 8% of the salary as a bonus.
They also consider giving a 2% bonus to all employees whose salaries are not greater than Rs.
25,000. Write a Python program to input the employee number, name, salary and sex of an
employee and display the pay slip containing the required information in an acceptable format.

(PToC = 10 minutes)

'''
# Salary bonuses:
# male = 5%
# female = 8%
# all employees = 2% - if under 25,000 salary 


emp_no = int(input("Enter employee number: "))
emp_name = input("Enter employee name: ").capitalize()
emp_salary = float(input("Enter employee salary: "))
emp_sex = input("Enter employee sex (M/F): ").upper()

# Calculate bonus
if emp_sex == 'M':
    bonus = emp_salary * 0.05 # 0.05 = 5%
elif emp_sex == 'F':
    bonus = emp_salary * 0.08 # 0.08 = 8%

# Apply additional bonus if salary is not greater than Rs. 25,000
if emp_salary <= 25000:
    bonus = bonus + emp_salary * 0.02 # 0.02 = 2%
    # bonus += emp_salary * 0.02 # in shorthand 

# Calculate total pay
total_pay = emp_salary + bonus

# display the pay slip
print("\n_____Employee Pay Slip_____")
print(f"Employee Number : {emp_no}")
print(f"Employee Name : {emp_name}")
print(f"Employee Salary is : {emp_salary}, Bonus is {bonus} and Total pay is {total_pay}")
print(f"Employee Sex : {emp_sex}")






########################################################################

# gender = input("Gender: ")
# salary =float(input("Salary: "))
# # bonus = float(input("Bonus: "))

# if gender == 'M' or gender == 'm':
#     if salary > 25000:
#         bonus = float(salary * 0.05) # 0.05 = 5%
#     else:
#         bonus = float(salary * 0.02) # 0.02 = 2%

# if gender == 'F' or gender == 'f':
#     if salary > 25000:
#         bonus = float(salary * 0.08) # 0.05 = 8%, 0.1 = 10% 
#     else:
#         bonus = float(salary * 0.02) # 0.02 = 2%

# salary += bonus
# print(salary, bonus)



########################################################################
