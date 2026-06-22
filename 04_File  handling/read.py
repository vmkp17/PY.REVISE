#A file is a permanent storage unit used to store data.

#Reading means getting data from a file.

#example  
'''student.txt
FIFA
20
AIML
9.0 '''

# reading.py
import os

print(os.getcwd())
file = open("student.txt", "r")

data = file.read()

print(data)

file.close()