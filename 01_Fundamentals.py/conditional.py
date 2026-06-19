#if executes a block of code only when the condition is True
age = 20
if age >= 18:
    print("You can vote")


# if-else executes one block of code when the condition is True and another block when the condition is False
age = 15
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# if-elif-else executes one block of code among multiple conditions
marks = 85
if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")


#nested if-else is an if-else statement inside another if-else statement
age = 20

if age >= 18:

    if age >= 21:
        print("Can drink in some countries")

    else:
        print("Adult but under 21")

