#Sending data FROM program INTO file.
#eg: 
'''file = open("notes.txt","w")

file.write("Hello FIFA")

file.close()'''

#EXAMPLE
''' w Mode
Means:
Delete everything
Then write new data

Before:
Python
Java
AI'''

'''file = open("student.txt","w")
file.write("FIFA")'''

import os

print(os.getcwd())

file = open("student.txt","w")
file.write("FIFA")
file.close()