import csv

with open("data.csv","r") as infile, open("high_earners.csv", "w", newline="") as outfile, open ("low_earners.csv", "w", newline="") as outfile_2: 
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer_2 = csv.writer(outfile_2)
    header = next(reader)
    writer.writerow(header)
    writer_2.writerow(header)

    for row in reader:
        name = row[0]

        try:
            salary = int(row[2])
        except:
            continue

        if salary >= 4000:
            writer.writerow(row)
        else:
            writer_2.writerow(row)
