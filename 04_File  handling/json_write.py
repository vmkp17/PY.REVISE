import json

student = {
    "name": "madhuri",
    "age": 20,
    "cgpa": 9.0
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON File Created")