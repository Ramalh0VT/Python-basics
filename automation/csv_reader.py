import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "Ana":
            print(f"Ana earns {row[2]}")
        

