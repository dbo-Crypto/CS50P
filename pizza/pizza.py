import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len (sys.argv) > 2:
     sys.exit("Too many command-line arguments")
else:
    filename = sys.argv[1]
    table = []
    splited_filename = filename.split(".")
    if len(splited_filename) != 2 or splited_filename[1] != "csv":
        sys.exit("Not a CSV file")
    try:
        with open(filename) as file:
            for line in file:
                row = line.rstrip().split(",")
                table.append(row)
            header = table[0]
            table.pop(0)
            print(tabulate(table,headers=header, tablefmt="grid"))
    except FileNotFoundError:
          sys.exit("File not found")