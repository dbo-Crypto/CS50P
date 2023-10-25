import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len (sys.argv) > 3:
     sys.exit("Too many command-line arguments")
else:
    before = sys.argv[1]
    after = sys.argv[2]

    cleaned = []
    first_name = []
    last_name = []
    house = []

    splited_before = before.split(".")
    splited_after = after.split(".")
    if len(splited_before) != 2 or splited_before[1] != "csv" or len(splited_before) != 2 or splited_before[1] != "csv":
        sys.exit("Not a CSV file")
    try:
        with open(before) as file:
            spamreader = csv.reader(file, delimiter=' ')
            for row in spamreader:
                row = ','.join(row).replace(" ","")
                row = row.split(",")
                cleaned.append(row)
            cleaned.pop(0)

            first_name.append("first")
            last_name.append("last")
            house.append("house")


            for i in cleaned:
                first_name.append(i[1])
                last_name.append(i[0])
                house.append(i[2])

            with open(after, "w") as file2:
                for k in range(0,len(house)):
                    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                    writer.writerow({"first": first_name[k], "last": last_name[k], "house": house[k]})

    except FileNotFoundError:
          sys.exit("File not found")