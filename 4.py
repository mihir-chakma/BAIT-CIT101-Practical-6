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

# all employees = 2% - whose salaries under 25,000 


emp_no = int(input("Enter employee number: "))
emp_name = input("Enter employee name: ").capitalize()
emp_salary = float(input("Enter employee salary: "))
emp_sex = input("Enter employee sex (M/F): ").capitalize()

# Calculate bonus
if emp_sex == 'M' or emp_sex == "Male":
    bonus = emp_salary * 0.05 # 0.05 = 5%
elif emp_sex == 'F' or emp_sex == "Female":
    bonus = emp_salary * 0.08 # 0.08 = 8%
    
# Apply additional bonus if salary is not greater than Rs. 25,000
if emp_salary < 25000:
    # bonus += emp_salary * 0.02 # 0.02 = 2%
    bonus = bonus + emp_salary * 0.02

# Calculate total pay
total_pay = emp_salary + bonus

# display the pay slip
print(f"\n___Employee Pay Slip___")
print(f"Employee Number : {emp_no}")
print(f"Employee Name   : {emp_name}")
print(f"Employee Salary is {emp_salary}, Bonus is {bonus} and Total payment is: {total_pay:.2f}")
print(f"Employee Sex    : {emp_sex}")

