# What is an Operator?
#An operator is a symbol that performs an operation on one or more values (operands).
'''a = 10
b = 5
print(a + b)
'''
# Types of Operators
''' 
1.Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators'''

# Student Information & Eligibility Checker

# Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))
backlog = int(input("Enter number of backlogs: "))

# Arithmetic Operators
next_age = age + 1

# Comparison Operators
is_adult = age >= 18
is_good_cgpa = cgpa >= 8

# Logical Operators
placement_eligible = (cgpa >= 8) and (backlog == 0)

# Output
print("\n----- STUDENT REPORT -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")
print(f"Backlogs: {backlog}")

print("\n----- RESULTS -----")
print(f"Next Year Age: {next_age}")
print(f"Adult: {is_adult}")
print(f"Good CGPA: {is_good_cgpa}")
print(f"Placement Eligible: {placement_eligible}")