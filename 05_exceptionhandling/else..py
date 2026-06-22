#Runs ONLY when no exception occurs.

try:

    num = int(input("Enter Number: "))

except ValueError:

    print("Invalid Input")

else:

    print("Valid Number")
