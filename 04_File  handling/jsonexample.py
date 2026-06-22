import json

name = input("Enter Name: ")
age = int(input("Enter Age: "))
cgpa = float(input("Enter CGPA: "))

student = {
    "name": name,
    "age": age,
    "cgpa": cgpa
}

with open("example.json", "w") as file:
    json.dump(student, file, indent=4)
    

print("Profile Saved")