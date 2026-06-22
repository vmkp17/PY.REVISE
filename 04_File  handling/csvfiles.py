#Comma Separated Values

#reading csv files
import csv

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


#writing csv files
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Age"])

    writer.writerow(["FIFA",20])