import csv
import sys

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader) #skip header
    
    for row in reader:
        name = row[0]
        try:
            salary = int(row[2])
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()
        age = row[1]

        if salary >= 4000:
            print(f"{name} is {age} years old and earns {salary}")
